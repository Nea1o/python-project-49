import prompt


def number_of_attempts(counter=3):
    return counter


def comparison_of_answer(answer, true_answer, name):
    if answer == true_answer:
        print('Correct!')
        return 'Correct!'
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was "
              f"{true_answer}.")
        print(f"Let's try again, {name}!")
        return ''


def cycle(logic_game, name_user):
    name = name_user
    result = ""
    count = 0
    count_try = number_of_attempts()
    while count < count_try:
        true_answer = logic_game()
        answer = prompt.string("Your answer? ")
        result = comparison_of_answer(answer, true_answer, name)
        if result == 'Correct!':
            count += 1
        else:
            break
        if count == count_try:
            result = f"Congratulations, {name}!"
            break
    print(result)
