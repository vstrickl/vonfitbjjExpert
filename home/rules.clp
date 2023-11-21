(deftemplate message
    (slot text)
)

(defrule hello-world
    => 
    (assert (message (text "Hello from CLIPS!")))
)