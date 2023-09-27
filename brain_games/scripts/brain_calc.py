import random
from brain_games.cli import welcome_user
from brain_games.cli import comparison_of_answer
import prompt


def main():
    name = welcome_user()
    result = ""
    print('What is the result of the expression?')
    count = 0
    while count < 3:
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
        answer = prompt.string("Your answer? ")
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
