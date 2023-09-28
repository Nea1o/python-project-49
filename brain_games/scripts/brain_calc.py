from brain_games.cli import welcome_user, number_of_attempts, comparison_of_answer
import random
import prompt


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    result = ""
    count = 0
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
    # игра складывает 2 случайных числа от 1 до 25
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    formulas_list = ["-", "+", "*"]
    formulas = random.choice(formulas_list)
    if formulas == "-":
        true_answer = str(num_1 - num_2)
    elif formulas == "+":
        true_answer = str(num_1 + num_2)
    else:
        true_answer = str(num_1 * num_2)
    print(f'Question: {num_1} {formulas} {num_2}')
    return true_answer


if __name__ == "__main__":
    main()
