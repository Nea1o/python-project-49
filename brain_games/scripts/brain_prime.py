from brain_games.cli import welcome_user, number_of_attempts, comparison_of_answer
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
    # игра которая отвечает на вопрос просто число или нет
    number = random.randint(1, 50)
    print(f'Question: {number}')
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            return 'no'
    return 'yes'


if __name__ == "__main__":
    main()
