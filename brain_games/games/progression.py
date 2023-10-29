import random


def executing_cycle_progression():
    num_begin = random.randint(MIN_NUM_BEGIN, MAX_NUM_BEGIN)
    step = random.randint(STEP_MIN, STEP_MAX)
    len_progression = random.randint(STEP_MIN, STEP_MAX)
    list_question = [num_begin]
    for i in range(len_progression):
        list_question.append(list_question[-1] + step)
    secret_number = random.randint(MIN_SECRET_NUM, len_progression)
    true_answer = str(list_question[secret_number])
    list_question[secret_number] = ".."
    print('Question: ', end="")
    print(*list_question)
    return true_answer


MIN_NUM_BEGIN = 1
MAX_NUM_BEGIN = 20
STEP_MIN = 1
STEP_MAX = 10
MIN_SECRET_NUM = 0
