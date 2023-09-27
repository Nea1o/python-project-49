from brain_games.cli import welcome_user
from brain_games.cli import comparison_of_answer
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    result = ""
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string("your answer? ")
        for i in range(2, number // 2):
            if number % i == 0:
                true_answer = 'no'
                break
            else:
                true_answer = 'yes'
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
