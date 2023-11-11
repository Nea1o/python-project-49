#!/usr/bin/python

from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games.calc import generating_game_calc, QUEST


def main():
    name = welcome_user()
    run_game(generating_game_calc, QUEST, name)


if __name__ == "__main__":
    main()
