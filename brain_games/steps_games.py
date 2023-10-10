import random


def game_step_calc():
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


def game_step_even():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_step_gcd():
    num_1 = random.randint(1, 30)
    num_2 = random.randint(1, 30)
    print(f'Question: {num_1} {num_2}')
    min_value = min([num_1, num_2])
    for elem in list(range(min_value + 1))[::-1]:
        if num_1 % elem == 0 and num_2 % elem == 0:
            return str(elem)


def game_step_prime():
    number = random.randint(1, 50)
    print(f'Question: {number}')
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return 'no'
    return 'yes'


def game_step_progression():
    num_begin = random.randint(1, 20)
    step = random.randint(1, 10)
    len_progression = random.randint(4, 14)
    list_question = [num_begin]
    for i in range(len_progression):
        list_question.append(list_question[-1] + step)
    secret_numer = random.randint(0, len_progression)
    true_answer = str(list_question[secret_numer])
    list_question[secret_numer] = ".."
    print('Question: ', end="")
    print(*list_question)
    return true_answer
