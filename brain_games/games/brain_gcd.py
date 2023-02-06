#!/usr/bin/env python3
import brain_games.scripts.engine
import random
import math


question = 'Find the greatest common divisor of given numbers.'
def game_question():
    global num1
    global num2
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Question: {num1} {num2}')


def is_correct_answer():
    correct_answer = str(math.gcd(num1, num2))
    return correct_answer

def main():
    brain_games.scripts.engine.greet()
    brain_games.scripts.engine.ask_question(question)
    brain_games.scripts.engine.run_game(game_question, is_correct_answer)

if __name__ == '__main__':
    main()
