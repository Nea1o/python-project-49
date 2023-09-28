from brain_games.cli import welcome_user, number_of_attempts, comparison_of_answer
import random
import prompt


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
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
    num_1 = random.randint(1, 30)
    num_2 = random.randint(1, 30)
    print(f'Question: {num_1} {num_2}')
    min_value = min([num_1, num_2])
    for elem in list(range(min_value + 1))[::-1]:
        if num_1 % elem == 0 and num_2 % elem == 0:
            return str(elem)


if __name__ == "__main__":
    main()
