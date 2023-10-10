from brain_games.cli import welcome_user
from brain_games.engine import (number_of_attempts, comparison_of_answer)
from brain_games.steps_games import game_step_progression
import prompt


def progression_game():
    """игра выдающая случайную прогрессию с одним
         неизвестным числом с случайным шагом от 1 до 10,
          и случайной длинной прогрессии от 4 до 14 чисел"""
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 0
    result = ""
    COUNT_TRY = number_of_attempts()
    while count < COUNT_TRY:
        true_answer = game_step_progression()
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
