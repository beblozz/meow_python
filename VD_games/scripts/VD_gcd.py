import random
import math
from ..cli import welcome_user

def find_gcd(a, b):
    return math.gcd(a, b)

def play_gcd_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)
        print(f"Question: {num1} {num2}")
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
    play_gcd_game()

if __name__ == "__main__":
    main()
