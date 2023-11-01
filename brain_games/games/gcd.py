#!/usr/bin/python

import random


def executing_cycle_gcd():
    print(QUEST)
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {num_1} {num_2}')
    return get_answer_gcd(num_1, num_2)


def get_answer_gcd(num1, num2):
    min_value = min([num1, num2])
    for elem in list(range(min_value + 1))[::-1]:
        if num1 % elem == 0 and num2 % elem == 0:
            return str(elem)


QUEST = ("Find the greatest "
         "common divisor of given numbers.")
MIN_NUM = 1
MAX_NUM = 30
