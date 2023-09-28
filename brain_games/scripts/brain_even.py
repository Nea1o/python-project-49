from brain_games.cli import (welcome_user, number_of_attempts,
                             comparison_of_answer)
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    result = ""
    COUNT_TRY = number_of_attempts()
    while count < COUNT_TRY:
        true_answer = game_step()
        answer = prompt.string("Your answer? ")
        result = comparison_of_answer(answer, true_answer, name)
        if result == 'Correct!':
            count += 1
        else:
            break
        if count == COUNT_TRY:
            result = f"Congratulations, {name}!"
            break
    print(result)


def game_step():
    # игра проверяет случайное число от 1 до 100 на чётность
    number = random.randint(1, 100)
    print(f'Question: {number}')
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == "__main__":
    main()
