#!/usr/bin/python

import prompt

COUNTER = 3


def run_game(get_answer_and_question, quest, name_user):
    name = name_user
    print(quest)
    for count in range(COUNTER):
        true_answer = get_answer_and_question()
        answer = prompt.string("Your answer? ")
        if answer != true_answer:
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"{true_answer}.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")
    return
