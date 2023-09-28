from brain_games.cli import (welcome_user, number_of_attempts,
                             comparison_of_answer)
import random
import prompt


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
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
    """игра выдающая случайную прогрессию с одним
     неизвестным числом с случайным шагом от 1 до 10,
      и случайной длинной прогрессии от 4 до 14 чисел"""
    num_begin = random.randint(1, 20)
    step = random.randint(1, 10)
    len_progression = random.randint(4, 14)
    list_question = [num_begin]
    for i in range(len_progression):
        list_question.append(list_question[-1] + step)
    secret_numer = random.randint(0, len_progression)
    true_answer = str(list_question[secret_numer])
    list_question[secret_numer] = ".."
    print('Question: ', end="")
    print(*list_question)
    return true_answer


if __name__ == "__main__":
    main()
