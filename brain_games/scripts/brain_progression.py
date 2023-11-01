#!/usr/bin/python

from brain_games.cli import welcome_user
from brain_games.engine import cycle
from brain_games.games.progression import executing_cycle_progression


def main():
    name = welcome_user()
    cycle(executing_cycle_progression, name)


if __name__ == "__main__":
    main()
