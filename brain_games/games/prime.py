import random


def game_logic_prime():
    number = random.randint(1, 50)
    print(f'Question: {number}')
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return 'no'
    return 'yes'
