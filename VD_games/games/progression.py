import random

GAME_RULE = "What number is missing in the progression?"

def generate_question():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = 10
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer
