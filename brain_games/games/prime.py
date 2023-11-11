#!/usr/bin/python

import random

QUEST = ('Answer "yes" if given number is prime.'
         ' Otherwise answer "no".')
MIN_NUM = 1
MAX_NUM = 50


def generating_game_prime():
    number = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {number}')
    if is_prime(number):
        return "yes"
    return "no"


def is_prime(number):
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return False
    return True
