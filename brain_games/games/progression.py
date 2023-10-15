import random


def game_logic_progression():
    num_begin = random.randint(1, 20)
    step = random.randint(1, 10)
    len_progression = random.randint(4, 14)
    list_question = [num_begin]
    for i in range(len_progression):
        list_question.append(list_question[-1] + step)
    secret_number = random.randint(0, len_progression)
    true_answer = str(list_question[secret_number])
    list_question[secret_number] = ".."
    print('Question: ', end="")
    print(*list_question)
    return true_answer
