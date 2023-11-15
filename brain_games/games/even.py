#!/usr/bin/python

import random

QUEST = ('Answer "yes" if the number'
         ' is even, otherwise answer "no".')
MIN_NUM = 1
MAX_NUM = 100


def generate_game_even():
    number = random.randint(MIN_NUM, MAX_NUM)
    if number % 2 == 0:
        return 'yes', f'Question: {number}'
    return 'no', f'Question: {number}'
