From Stdlib Require Import List String.
From Warblre Require Import Inst API Patterns Result Frontend.
Import ListNotations.
Import Patterns.Patterns.
Import NaiveEngine.
Open Scope string_scope.

(* Explicit AST feasibility probe using upstream's ASCII-oriented NaiveEngine.
   This is NOT an as-written proof: source parsing/correspondence and concrete
   full UTF-16 canonicalization are undischarged. No consumer gate uses this. *)
Definition codes (s : String.string) : list nat :=
  List.map Byte.to_nat (String.list_byte_of_string s).
Definition chars (s : String.string) : NaiveEngine.Regex :=
  List.fold_right (fun n tail => Seq (Char n) tail) Empty (codes s).
Definition names : list String.string :=
  ["dnsmasq";"procd";"ubusd";"netifd";"odhcpd";"logd";
   "dropbear";"uhttpd";"hostapd";"wpad"].
Definition alternatives : NaiveEngine.Regex :=
  match List.map chars names with
  | [] => Empty
  | h::t => List.fold_left Disjunction t h
  end.
Definition continuation : NaiveEngine.Regex :=
  CharacterClass (InvertedCC
    (RangeCR (SourceCharacter 65) (SourceCharacter 90)
    (RangeCR (SourceCharacter 97) (SourceCharacter 122)
    (RangeCR (SourceCharacter 48) (SourceCharacter 57)
    (ClassAtomCR (SourceCharacter 95)
    (ClassAtomCR (SourceCharacter 45) EmptyCR)))))).
Definition prefix_ast : NaiveEngine.Regex :=
  Seq InputStart
    (Seq (Group None alternatives)
         (Group None (Disjunction continuation InputEnd))).
(* The Unicode field is unit: tt is not a proof of a concrete non-/u mode. *)
Definition i_only_flag_record : RegExpFlags :=
  RegExpFlags.make false false true false false tt false.
Definition probe (s : String.string) : option bool :=
  match NaiveEngine.initialize prefix_ast i_only_flag_record with
  | Success r =>
      match NaiveEngine.test r (codes s) with
      | Success (b,_) => Some b
      | Error _ => None
      end
  | Error _ => None
  end.

Example mixed_case_bracket : probe "WpAd[" = Some true.
Proof. vm_compute. reflexivity. Qed.
Example hyphen_is_continuation : probe "wpad-drop" = Some false.
Proof. vm_compute. reflexivity. Qed.
Example bracket_is_boundary : probe "wpad[" = Some true.
Proof. vm_compute. reflexivity. Qed.
Example anchored : probe "xwpad[" = Some false.
Proof. vm_compute. reflexivity. Qed.
Print Assumptions mixed_case_bracket.
Print Assumptions hyphen_is_continuation.
