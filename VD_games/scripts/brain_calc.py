import random
from ..cli import welcome_user

def calculate_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2

def play_calc_game():
    name = welcome_user()
    print("What is the result of the expression?")
    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        correct_answer = calculate_expression(num1, num2, operator)
        print(f"Question: {num1} {operator} {num2}")
        user_answer = input("Your answer: ").strip()
        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

def main():
    play_calc_game()

if __name__ == "__main__":
    main()
