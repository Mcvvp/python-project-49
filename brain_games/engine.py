import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    print(game.rule)
    name = greet()
    correct_answers_count = 0
    limit_of_rounds = 3
    while correct_answers_count < limit_of_rounds:
        question, correct_answer = game.game_core()
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                + f'Correct answer was "{correct_answer}".'
                + f'\nLet\'s try again, {name}!')
            break
        if correct_answers_count == limit_of_rounds:
            print(f'Congratulations, {name}!')
