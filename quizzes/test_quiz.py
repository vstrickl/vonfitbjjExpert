import os

from clips import Environment

def run_quiz():
    environment = Environment()

    # Load and run the CLIPS environment
    module_dir = os.path.dirname(__file__)
    clips_file = os.path.join(module_dir, 'nfl_quiz.clp')
    environment.load(clips_file)

    # Initialize the quiz
    environment.reset()

    # Interact with the user
    for fact in environment.facts():
        if fact.template.name == "question":
            q_text = fact['text']
            q_id = fact['id']
            option_a = fact['option-a']
            option_b = fact['option-b']
            option_c = fact['option-c']
            option_d = fact['option-d']
            print(f"Question {q_id}: {q_text}")
            print(f" a) {option_a}\n b) {option_b}\n c) {option_c}\n d) {option_d}")
            user_answer = input("Your answer: ")
            response_fact = f"(response (question-id {q_id}) (answer \"{user_answer}\"))"
            environment.assert_string(response_fact)

    # Run the quiz
    environment.run()

    # Retrieve the score
    for fact in environment.facts():
        if fact.template.name == "score":
            correct = fact['correct']
            incorrect = fact['incorrect']
            total_questions = correct + incorrect
            accuracy = round((correct / total_questions) * 100, 2) if total_questions > 0 else 0.0
            print(f"\nQuiz Finished.\nTotal Correct: {correct}\nTotal Incorrect: {incorrect}\nYour Score: {accuracy}%")

if __name__ == "__main__":
    run_quiz()
