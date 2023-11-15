#!/usr/bin/python

import random

QUEST = "What is the result of the expression?"
MIN_NUM = 1
MAX_NUM = 25
FORMULAS_LIST = ("+", "-", "*")


def generate_game_calc():
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    formulas = random.choice(FORMULAS_LIST)
    true_answer = calculate(num_1, num_2, formulas)
    return true_answer, f"Question: {num_1} {formulas} {num_2}"


def calculate(num1, num2, symbol):
    if symbol == "-":
        return str(num1 - num2)
    if symbol == "+":
        return str(num1 + num2)
    return str(num1 * num2)
