from brain_games.cli import welcome_user
from brain_games.engine import (number_of_attempts, comparison_of_answer)
from brain_games.steps_games import game_step_even
import prompt


def even_game():
    # игра проверяет случайное число от 1 до 100 на чётность
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    result = ""
    COUNT_TRY = number_of_attempts()
    while count < COUNT_TRY:
        true_answer = game_step_even()
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
