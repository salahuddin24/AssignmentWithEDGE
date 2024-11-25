# [Your Name]_assignment1.py

def simple_quiz():
    print("Welcome to the Simple Quiz!")
    print("Each correct answer awards 5 points.")
    print("Each incorrect answer deducts 2 points.")
    print("You need 60% or higher to pass. Let's begin!\n")

    # Quiz questions and their correct answers
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 12 divided by 4?", "answer": "3"},
        {"question": "Which planet is known as the Blue Planet?", "answer": "Earth"},
        {"question": "Who painted the Mona Lisa?", "answer": "Da Vinci"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"}
    ]

    # Initialize quiz variables
    total_questions = len(questions)
    points_per_correct = 5
    points_per_wrong = -2
    total_score = 0

    # Quiz logic
    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == q["answer"].lower():
            print("Correct! +5 points.\n")
            total_score += points_per_correct
        else:
            print(f"Wrong! The correct answer was: {q['answer']}. -2 points.\n")
            total_score += points_per_wrong

    # Calculate passing score
    passing_score = 0.6 * (total_questions * points_per_correct)

    # Display results
    print(f"Your total score: {total_score}/{total_questions * points_per_correct}")
    if total_score >= passing_score:
        print("Congratulations! You passed the quiz. 🎉")
    else:
        print("You failed the quiz. Better luck next time! 😢")

# Run the quiz
if __name__ == "__main__":
    simple_quiz()
