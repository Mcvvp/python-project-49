#!/usr/bin/env python3
import random


rule = 'What is the result of the expression?'


def game_core():
    var_exp = ['+', '-', '*']
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    exp = random.choice(var_exp)
    question = f'Question: {num1} {exp} {num2}'
    if exp == '+':
        correct_answer = str(num1 + num2)
    elif exp == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return question, correct_answer
