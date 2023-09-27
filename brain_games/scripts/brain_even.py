import random
from brain_games.cli import welcome_user
from brain_games.cli import comparison_of_answer
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    result = ""
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string("your answer? ")
        if number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        result = comparison_of_answer(answer, true_answer, name)
        if result == 'Correct!':
            count += 1
        else:
            break
        if count == 3:
            result = f"Congratulations, {name}!"
            break
    print(result)


if __name__ == "__main__":
    main()
