#!/usr/bin/python

from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games.prime import generate_game_prime, QUEST


def main():
    run_game(generate_game_prime, QUEST, name=welcome_user())


if __name__ == "__main__":
    main()
