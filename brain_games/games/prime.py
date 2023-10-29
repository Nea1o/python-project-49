import random


def executing_cycle_prime():
    number = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {number}')
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return 'no'
    return 'yes'


MIN_NUM = 1
MAX_NUM = 50
