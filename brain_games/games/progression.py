#!/usr/bin/python

import random

QUEST = "What number is missing in the progression?"
MIN_NUM_BEGIN = 1
MAX_NUM_BEGIN = 20
STEP_MIN = 1
STEP_MAX = 10
LEN_MIN = 5
LEN_MAX = 14
MIN_SECRET_NUM = 0


def generate_game_progression():
    num_begin = random.randint(MIN_NUM_BEGIN, MAX_NUM_BEGIN)
    step = random.randint(STEP_MIN, STEP_MAX)
    len_progression = random.randint(LEN_MIN, LEN_MAX)
    list_question = get_progression(num_begin, step, len_progression)
    secret_number = random.randint(MIN_SECRET_NUM, len_progression)
    true_answer = str(list_question[secret_number])
    list_question[secret_number] = ".."
    return true_answer, 'Question: ' + ' '.join(map(str, list_question))


def get_progression(num_begin, step, len_progression):
    lst = [num_begin]
    for i in range(len_progression):
        lst.append(lst[-1] + step)
    return lst
