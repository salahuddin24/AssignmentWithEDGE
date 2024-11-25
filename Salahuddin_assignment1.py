


def simple_quiz():
    print("Welcome to the Simple Quiz!")
    print("Each correct answer awards 5 points.")
    print("Each incorrect answer deducts 2 points.")
    print("You need 60% or higher to pass. Let's begin!")

    # Quiz questions and their correct answers
    question = [
        {"question":"What is the capital of France?", "answer":"Paris"},
        {"question":"What is 12 divided by 4?", "answer" : "3"},
        {"question":"What is the chemical symbol for water?", "answer":"H2O"},
        {"question":"What is the capital of Bangladesh?", "answer":"Dhaka"},
        {"question":"What is the currency of Bangladesh?", "answer":"Taka"}
    ]
    # quiz variable
    total_question = len(question)
    points_per_correct = 5
    points_per_wrong = -2
    total_score = 0

    # quiz logic

    print("Question 1 :",question[0]["question"])
    user_ans_1 = input()
    if user_ans_1.lower() == question[0]["answer"].lower():
        print("Correct! +5 points. \n")
        total_score += points_per_correct
    else:
        print(f"Wrong! The correct answer was : {question[0]["answer"]}")
        total_score += points_per_wrong


    print("Question 2 :", question[1]["question"])
    user_ans_2 = input()
    if user_ans_2.lower() == question[1]["answer"].lower():
        print("Correct! +5 points. \n")
        total_score += points_per_correct
    else:
        print(f"Wrong! The correct answer was : {question[1]["answer"]}")
        total_score += points_per_wrong

    print("Question 3 :", question[2]["question"])
    user_ans_3 = input()
    if user_ans_3.lower() == question[2]["answer"].lower():
        print("Correct! +5 points. \n")
        total_score += points_per_correct
    else:
        print(f"Wrong! The correct answer was : {question[2]["answer"]}")
        total_score += points_per_wrong

    print("Question 4 :", question[3]["question"])
    user_ans_4 = input()
    if user_ans_4.lower() == question[3]["answer"].lower():
        print("Correct! +5 points. \n")
        total_score += points_per_correct
    else:
        print(f"Wrong! The correct answer was : {question[3]["answer"]}")
        total_score += points_per_wrong

    print("Question 5 :", question[4]["question"])
    user_ans_5 = input()
    if user_ans_5.lower() == question[4]["answer"].lower():
        print("Correct! +5 points. \n")
        total_score += points_per_correct
    else:
        print(f"Wrong! The correct answer was : {question[4]["answer"]}")
        total_score += points_per_wrong

    # passing score
    passing_score = 0.6 * (total_question*points_per_correct)
    # print(passing_score)

    # display the result
    print(f"Your total score : {total_score}/{total_question*points_per_correct}")
    if total_score >= passing_score:
        print("Congratulations! You passed the quiz. 🎉")
    else:
        print("You failed the quiz. Better luck next time! 😢")


simple_quiz()


