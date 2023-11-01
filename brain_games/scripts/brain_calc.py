#!/usr/bin/python

from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.calc import executing_cycle_calc


def main():
    name = welcome_user()
    cycle(executing_cycle_calc, name)


if __name__ == "__main__":
    main()
