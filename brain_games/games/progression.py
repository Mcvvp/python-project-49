#!/usr/bin/env python3
import random


rule = 'What number is missing in the progression?'


def game_core():
    progression_step = random.randint(1, 5)
    progression_length = random.randint(5, 10)
    progression = []
    first_elem = random.randint(1, 50)
    progression.append(first_elem)
    counter = 0
    while counter < progression_length - 1:
        progression.append(progression[counter] + progression_step)
        counter += 1
    rand_elem = random.choice(progression)
    correct_answer = str(rand_elem)
    string_progression = ''
    progression_counter = 0
    while progression_counter < progression_length:
        string_progression += str(progression[progression_counter]) + ' '
        progression_counter += 1
    result = string_progression.replace(str(correct_answer), "..").strip()
    question = f'Question: {result}'
    return question, correct_answer
