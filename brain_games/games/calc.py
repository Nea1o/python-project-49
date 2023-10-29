import random


def executing_cycle_calc():
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    formulas_list = (MINUS, PLUS, MULTIPLICATION)
    formulas = random.choice(formulas_list)
    true_answer = calc_exe(num_1, num_2, formulas)
    print(f'Question: {num_1} {formulas} {num_2}')
    return true_answer


def calc_exe(num1, num2, symbol):
    if symbol == "-":
        return str(num1 - num2)
    if symbol == "+":
        return str(num1 + num2)
    return str(num1 * num2)


MIN_NUM = 1
MAX_NUM = 25
PLUS = "+"
MINUS = "-"
MULTIPLICATION = "*"
