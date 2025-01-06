(defglobal ?*mrsCon* = ls-uc)
(defglobal ?*mrs-dbug* = ls-uc-dbug)

(defrule updateConcepts
(id-lsl	 ?id	 ?lanspec)
(cl-ls-mrs ?conLabel ?lanspec ?mrsConcept)
=>
(printout ?*mrsCon* "(id-cl	 "?id"	 "?conLabel")"crlf)
(printout ?*mrs-dbug* "(rule-rel-values updateConcepts id-cl	 "?id"	 "?conLabel")"crlf)
)

(defrule updateTAM
(kriyA-TAM	 ?id2	 ?lanspectam)
(U_TAM-LS_TAM-Perfective_Aspect-Progressive_Aspect-Tense-Modal ?uni_label ?lanspectam $?var)
=>
(printout ?*mrsCon* "(kriyA-TAM	 "?id2"	 "?uni_label")"crlf)
(printout ?*mrs-dbug* "(rule-rel-values updateTAM kriyA-TAM	 "?id2"	 "?uni_label")"crlf)
)

(defrule printFacts
(declare (salience -9000))
?f<-(USRinfo $?vars)
=>
(retract ?f)
(printout ?*mrsCon* "("(implode$ (create$ $?vars))")" crlf)
(printout ?*mrs-dbug* "(rule-rel-values printFacts "(implode$ (create$ $?vars))")"crlf)
)
