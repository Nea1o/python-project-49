from brain_games.cli import welcome_user
from brain_games.engine import (number_of_attempts, comparison_of_answer)
from brain_games.steps_games import game_step_prime
import prompt


def prime_game():
    # игра которая отвечает на вопрос простое число или нет
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    result = ""
    COUNT_TRY = number_of_attempts()
    while count < COUNT_TRY:
        true_answer = game_step_prime()
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
