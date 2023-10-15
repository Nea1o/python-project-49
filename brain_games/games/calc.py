import random


def game_logic_calc():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    formulas_list = ["-", "+", "*"]
    formulas = random.choice(formulas_list)
    if formulas == "-":
        true_answer = str(num_1 - num_2)
    elif formulas == "+":
        true_answer = str(num_1 + num_2)
    else:
        true_answer = str(num_1 * num_2)
    print(f'Question: {num_1} {formulas} {num_2}')
    return true_answer
