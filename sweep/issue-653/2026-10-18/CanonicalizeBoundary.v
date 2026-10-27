From Stdlib Require Import List Arith Bool Lia.
Import ListNotations.

(* Research sublemma, not a complete ECMAScript or fwlive theorem.
   upper_units stands for the UTF-16 encoding of Unicode Default Uppercase.
   Its implementation, its specification correspondence, the regex parser,
   and the Warblre parameter instantiation are NOT proved here.
   This isolates the non-/u Canonicalize return logic (ECMA-262 2023,
   22.2.2.7.3 steps 5-10) when IgnoreCase is true. *)
Definition non_u_canonicalize
    (upper_units : nat -> list nat) (ch : nat) : nat :=
  match upper_units ch with
  | [cu] =>
      if (128 <=? ch) && (cu <? 128) then ch else cu
  | _ => ch
  end.

(* Crucially independent of the particular Unicode uppercase table. *)
Theorem non_ascii_stays_non_ascii :
  forall upper_units ch,
    128 <= ch -> 128 <= non_u_canonicalize upper_units ch.
Proof.
  intros upper_units ch Hch.
  unfold non_u_canonicalize.
  destruct (upper_units ch) as [|cu rest]; [exact Hch|].
  destruct rest as [|next rest]; [|exact Hch].
  assert ((128 <=? ch) = true) as Hge by (apply Nat.leb_le; exact Hch).
  rewrite Hge. simpl.
  destruct (cu <? 128) eqn:Hlt; [exact Hch|].
  apply Nat.ltb_ge in Hlt. exact Hlt.
Qed.

Corollary ascii_output_requires_ascii_input :
  forall upper_units ch,
    non_u_canonicalize upper_units ch < 128 -> ch < 128.
Proof.
  intros upper_units ch Hout.
  destruct (Nat.lt_ge_cases ch 128) as [Hlt|Hge]; [exact Hlt|].
  pose proof (non_ascii_stays_non_ascii upper_units ch Hge). lia.
Qed.

(* These are finite facts about this return-logic definition. *)
Example long_s_never_becomes_ascii_s :
  non_u_canonicalize (fun _ => [83]) 383 = 383.
Proof. reflexivity. Qed.

Example multi_unit_uppercase_returns_original :
  non_u_canonicalize (fun _ => [83;83]) 223 = 223.
Proof. reflexivity. Qed.

Print Assumptions non_ascii_stays_non_ascii.
Print Assumptions ascii_output_requires_ascii_input.
