(deftemplate question
    (slot id)
    (slot text)
    (slot options) 
    (slot answer)
) 

(deftemplate response
    (slot question-id)
    (slot answer)
)

(deftemplate score
    (slot correct)
    (slot incorrect)
)

(deffacts quiz-questions
    (question (id 1)
        (text "Who won the Superbowl for the 2022 season?")
        (options "New England Patriots|Green Bay Packers|Dallas Cowboys|Kansas City Chiefs")
        (answer "Kansas City Chiefs")
    )
    (question (id 2)
        (text "Who is the last quarterback to throw for 50 touchdowns?")
        (options "Aaron Rodgers|Tom Brady|Patrick Mahomes|Russell Wilson")
        (answer "Patrick Mahomes")
    )
    (question (id 3)
        (text "What team did John Madden coach for in the NFL?")
        (options "San Francisco 49ers|Chicago Bears|Pittsburgh Steelers|Oakland Raiders")
        (answer "Oakland Raiders")
    )
    (question (id 4)
        (text "Who holds the single season rushing record in the NFL?")
        (options "Barry Sanders|Adrian Peterson|Emmitt Smith|Eric Dickerson")
        (answer "Eric Dickerson")
    )
    (question (id 5)
        (text "Who was the first professional football player?")
        (options "Jim Thorpe|Red Grange|George Halas|William “Pudge” Heffelfinger")
        (answer "William “Pudge” Heffelfinger")
    )
    (question (id 6)
        (text "Which NFL team has won the most superbowls?")
        (options "Dallas Cowboys|San Francisco 49ers|Green Bay Packers|The Patriots")
        (answer "The Patriots")
    )
)

(defrule check-answer
    ?r <- (response (question-id ?id) (answer ?ans))
    ?q <- (question (id ?id) (answer ?correct-ans))
    ?s <- (score)
    (test (eq ?ans ?correct-ans))
    =>
    (retract ?r)
    (bind ?score (+ 1 (fact-slot-value ?s 'correct)))
    (modify ?s (correct ?score))
    (printout t "Correct! The answer to question " ?id " is indeed " ?ans "." crlf)
)

(defrule incorrect-answer
    ?r <- (response (question-id ?id) (answer ?ans))
    ?q <- (question (id ?id) (answer ?correct-ans))
    ?score-fact <- (score)
    (test (neq ?ans ?correct-ans))
    =>
    (retract ?r)
    (bind ?score (fact-slot-value ?score-fact 'incorrect))
    (modify ?score-fact (incorrect ?score))
    (printout t "Nice Try!!! The answer to question " ?id " is not " ?ans ", it is " ?correct-ans "." crlf)
)

(deffacts initial-score
   (score (correct 0) (incorrect 0))
)