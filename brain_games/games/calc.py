#!/usr/bin/python

import random


def executing_cycle_calc():
    print(QUEST)
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    formulas_list = (MINUS, PLUS, MULTIPLICATION)
    formulas = random.choice(formulas_list)
    true_answer = calc_exe(num_1, num_2, formulas)
    return true_answer


def calc_exe(num1, num2, symbol):
    print(f"Question: {num1} {symbol} {num2}")
    if symbol == "-":
        return str(num1 - num2)
    if symbol == "+":
        return str(num1 + num2)
    return str(num1 * num2)


QUEST = "What is the result of the expression?"
MIN_NUM = 1
MAX_NUM = 25
PLUS = "+"
MINUS = "-"
MULTIPLICATION = "*"
