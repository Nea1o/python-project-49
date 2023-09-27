from brain_games.cli import welcome_user
from brain_games.cli import comparison_of_answer
import random
import prompt


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    result = ""
    while count < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        print(f'Question: {num_1} {num_2}')
        answer = prompt.string("your answer? ")
        min_value = min([num_1, num_2])
        for elem in list(range(min_value + 1))[::-1]:
            if num_1 % elem == 0 and num_2 % elem == 0:
                true_answer = str(elem)
                break
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
