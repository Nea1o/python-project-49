from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.calc import game_logic_calc


def main():
    name = welcome_user(quest="What is the result of the expression?")
    cycle(game_logic_calc, name)


if __name__ == "__main__":
    main()
