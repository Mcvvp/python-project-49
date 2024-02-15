#!/usr/bin/env python3
import random
import math


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_core():
    num = random.randint(2, 100)
    question = f'Question: {num}'
    top_divider = math.trunc(math.sqrt(num))
    correct_answer = 'yes'
    if top_divider > 1:
        for i in range(2, top_divider + 1):
            if (num % i) == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
    return question, correct_answer
