from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.gcd import executing_cycle_gcd


def main():
    name = welcome_user(quest="Find the greatest "
                              "common divisor of given numbers.")
    cycle(executing_cycle_gcd, name)


if __name__ == "__main__":
    main()
