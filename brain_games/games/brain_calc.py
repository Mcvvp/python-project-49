#!/usr/bin/env python3
import brain_games.scripts.engine
import random


question = 'What is the result of the expression?'


def game_question():
    global num1
    global num2
    global exp
    var_exp = ['+', '-', '*']
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    exp = random.choice(var_exp)
    print(f'Question: {num1} {exp} {num2}')


def is_correct_answer():
    if exp == '+':
        correct_answer = str(num1 + num2)
    elif exp == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return correct_answer


def main():
    brain_games.scripts.engine.greet()
    brain_games.scripts.engine.ask_question(question)
    brain_games.scripts.engine.run_game(game_question, is_correct_answer)


if __name__ == '__main__':
    main()
