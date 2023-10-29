from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.even import executing_cycle_even


def main():
    name = welcome_user(quest='Answer "yes" if the number'
                              ' is even, otherwise answer "no".')
    cycle(executing_cycle_even, name)


if __name__ == "__main__":
    main()
