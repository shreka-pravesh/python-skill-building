import random
def quiz_game():
    questions = {
        "What is the capital of India?": "delhi",
        "Python was created by?": "guido van rossum",
        "What is 5 * 6?": "30",
        "Which keyword is used to define a function?": "def"
    }
    score = 0
    q_list = list(questions.items())
    random.shuffle(q_list)
    for q, ans in q_list:
        print("\n" + q)
        user = input("Your answer: ").lower()
        if user == ans:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Answer: {ans}")
    print(f"\nYour final score: {score}/{len(questions)}")
if __name__ == "__main__":
    quiz_game()
