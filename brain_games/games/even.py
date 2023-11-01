#!/usr/bin/python

import random


def executing_cycle_even():
    print(QUEST)
    number = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {number}')
    if number % 2 == 0:
        return 'yes'
    return 'no'


QUEST = ('Answer "yes" if the number'
         ' is even, otherwise answer "no".')
MIN_NUM = 1
MAX_NUM = 100
