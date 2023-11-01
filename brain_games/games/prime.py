#!/usr/bin/python

import random


def executing_cycle_prime():
    print(QUEST)
    number = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {number}')
    return is_prime(number)


def is_prime(number):
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return 'no'
    return 'yes'


QUEST = ('Answer "yes" if given number is prime.'
         ' Otherwise answer "no".')
MIN_NUM = 1
MAX_NUM = 50
