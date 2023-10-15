from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.prime import game_logic_prime


def main():
    name = welcome_user(quest='Answer "yes" if given number is prime.'
                              ' Otherwise answer "no".')
    cycle(game_logic_prime, name)


if __name__ == "__main__":
    main()
