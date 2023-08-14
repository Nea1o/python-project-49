import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    result = ""
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input()
        if number % 2 == 0 and str(answer).lower() == 'yes':
            print("correct")
        elif number % 2 == 1 and str(answer).lower() == 'no':
            print("correct")
        elif number % 2 == 0 and str(answer).lower() != 'yes':
            result = f"'{answer}' is wrong answer ;(. Correct answer was 'yes'"
            break
        else:
            result = f"'{answer}' is wrong answer ;(. Correct answer was 'no'"
            break
        if count == 2:
            result = f"Congratulations, {name}!"
            break
        count += 1
    print(result)


if __name__ == "__main__":
    main()
