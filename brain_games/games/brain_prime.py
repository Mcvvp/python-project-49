#!/usr/bin/env python3
import brain_games.scripts.engine
import random
import math


question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_question():
    global num
    num = random.randint(2, 100)
    print(f'Question: {num}')


def is_correct_answer():
    top_devider = math.trunc(math.sqrt(num))
    if top_devider > 1:
        for i in range(2, top_devider + 1):
            if (num % i) == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
    else:
        correct_answer = 'yes'
    return correct_answer


def main():
    brain_games.scripts.engine.greet()
    brain_games.scripts.engine.ask_question(question)
    brain_games.scripts.engine.run_game(game_question, is_correct_answer)


if __name__ == "__main__":
    main()
