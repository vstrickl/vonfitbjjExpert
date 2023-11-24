import os

from clips import Environment

def run_quiz():
    environment = Environment()

    # Load and run the CLIPS environment
    module_dir = os.path.dirname(__file__)
    clips_file = os.path.join(module_dir, 'nfl_quiz.clp')
    environment.load(clips_file)
    environment.reset()

    # Initialize the quiz
    environment.reset()

    # Interact with the user
    for fact in environment.facts():
        if fact.template.name == "question":
            q_text = fact['text']
            q_id = fact['id']
            print(f"Question: {q_text}")
            user_answer = input("Your answer: ")
            response_fact = f"(response (question-id {q_id}) (answer \"{user_answer}\"))"
            environment.assert_string(response_fact)

    # Run the quiz
    environment.run()

    # Retrieve the score
    score_fact = None
    for fact in environment.facts():
        if fact.template.name == "score":
            score_fact = fact
            break

    if score_fact:
        correct = score_fact['correct']
        incorrect = score_fact['incorrect']
        print(f"Score: {correct} correct, {incorrect} incorrect")

if __name__ == "__main__":
    run_quiz()
