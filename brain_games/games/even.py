import random


def executing_cycle_even():
    number = random.randint(MIN_NUM, MAX_NUM)
    print(f'Question: {number}')
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


MIN_NUM = 1
MAX_NUM = 100
