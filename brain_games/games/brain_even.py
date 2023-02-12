#!/usr/bin/env python3
import brain_games.scripts.engine
import random


question = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    global num
    num = random.randint(1, 100)
    print(f'Question: {num}')


def is_correct_answer():
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def main():
    brain_games.scripts.engine.greet()
    brain_games.scripts.engine.ask_question(question)
    brain_games.scripts.engine.run_game(game_question, is_correct_answer)


if __name__ == '__main__':
    main()
