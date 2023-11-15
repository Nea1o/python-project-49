#!/usr/bin/python

import random

QUEST = ('Answer "yes" if given number is prime.'
         ' Otherwise answer "no".')
MIN_NUM = 1
MAX_NUM = 50


def generate_game_prime():
    number = random.randint(MIN_NUM, MAX_NUM)
    if is_prime(number):
        return "yes", f'Question: {number}'
    return "no", f'Question: {number}'


def is_prime(number):
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return False
    return True
