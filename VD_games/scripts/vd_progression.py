from ..engine import run_game
from ..games.progression import generate_question, GAME_RULE

def main():
    run_game(GAME_RULE, generate_question)

if __name__ == "__main__":
    main()
