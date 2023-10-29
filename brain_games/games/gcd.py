import random


def executing_cycle_gcd():
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {num_1} {num_2}')
    min_value = min([num_1, num_2])
    for elem in list(range(min_value + 1))[::-1]:
        if num_1 % elem == 0 and num_2 % elem == 0:
            return str(elem)


MIN_NUM = 1
MAX_NUM = 30
