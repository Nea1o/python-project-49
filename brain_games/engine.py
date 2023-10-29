import prompt


def cycle(execution_of_logic_game, name_user):
    name = name_user
    for count in range(1, COUNTER + 1):
        true_answer = execution_of_logic_game()
        answer = prompt.string("Your answer? ")
        if answer != true_answer:
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"{true_answer}.")
            print(f"Let's try again, {name}!")
            return ''
        print('Correct!')
    print(f"Congratulations, {name}!")
    return ""


COUNTER = 3
