import prompt


def greet():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def ask_question(question):
    print(question)


def run_game(ask_game_question, is_correct_answer):
    correct_answers_count = 0
    while correct_answers_count < 3:
        ask_game_question()
        answer = prompt.string('Your answer: ')
        if answer == is_correct_answer():
            print('Correct!')
            correct_answers_count += 1
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                + f'Correct answer was "{is_correct_answer()}".'
                + f'\nLet\'s try again, {name}!')
            break
        if correct_answers_count == 3:
            print(f'Congratulations, {name}!')
