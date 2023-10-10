from brain_games.cli import welcome_user
from brain_games.engine import (number_of_attempts, comparison_of_answer)
from brain_games.steps_games import game_step_gcd
import prompt


def gcd_game():
    # находит общий делитель 2 чисел
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    result = ""
    COUNT_TRY = number_of_attempts()
    while count < COUNT_TRY:
        true_answer = game_step_gcd()
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
