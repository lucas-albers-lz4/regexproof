(declare-fun s () String)
(assert (= 1 (+ (str.indexof s " " 0) (str.to_int (str.substr s 0 (ite (str.contains " " s) 1 0))))))
(check-sat)
