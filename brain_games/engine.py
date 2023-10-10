def comparison_of_answer(answer, true_answer, name):
    if answer == true_answer:
        print('Correct!')
        return 'Correct!'
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was "
              f"{true_answer}.")
        print(f"Let's try again, {name}!")
        return ''


def number_of_attempts(counter=3):
    return counter
