from .cli import welcome_user

def run_game(game_rule, generate_question):
    name = welcome_user()
    print(game_rule)
    correct_answers = 0
    rounds_count = 3
    while correct_answers < rounds_count:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
