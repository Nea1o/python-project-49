from brain_games.cli import welcome_user
from brain_games.cli import comparison_of_answer
import random
import prompt


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 0
    result = ""
    while count < 3:
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
        answer = prompt.string("your answer? ")
        result = comparison_of_answer(answer, true_answer, name)
        if result == 'correct':
            count += 1
        else:
            break
        if count == 3:
            result = f"Congratulations, {name}!"
            break
    print(result)


if __name__ == "__main__":
    main()
