import prompt


def welcome_user(quest=""):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(quest)
    return name


if __name__ == "__main__":
    welcome_user()
