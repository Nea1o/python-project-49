import random


def game_logic_gcd():
    num_1 = random.randint(1, 30)
    num_2 = random.randint(1, 30)
    print(f'Question: {num_1} {num_2}')
    min_value = min([num_1, num_2])
    for elem in list(range(min_value + 1))[::-1]:
        if num_1 % elem == 0 and num_2 % elem == 0:
            return str(elem)
