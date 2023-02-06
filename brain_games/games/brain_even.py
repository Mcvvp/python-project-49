#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    correct_answers_count = 0
    while correct_answers_count < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            break
        if correct_answers_count == 3:
            print(f'Congratulations, {name}!')


def main():
    welcome_user()
    brain_even()


if __name__ == '__main__':
    main()
