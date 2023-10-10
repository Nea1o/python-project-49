from brain_games.cli import welcome_user
from brain_games.engine import (number_of_attempts, comparison_of_answer)
from brain_games.steps_games import game_step_calc
import prompt


def calc_game():
    # игра складывает 2 случайных числа от 1 до 25
    name = welcome_user()
    print('What is the result of the expression?')
    result = ""
    count = 0
    COUNT_TRY = number_of_attempts()
    while count < COUNT_TRY:
        true_answer = game_step_calc()
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
