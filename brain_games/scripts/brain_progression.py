from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.progression import game_logic_progression


def main():
    name = welcome_user(quest="What number is missing in the progression?")
    cycle(game_logic_progression, name)


if __name__ == "__main__":
    main()
