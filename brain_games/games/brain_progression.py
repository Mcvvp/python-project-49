#!/usr/bin/env python3
import brain_games.scripts.engine
import random


question = 'What number is missing in the progression?'


def game_question():
    global progression
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
    global random_answer
    random_answer = rand_elem
    progression = str(progression)
    progression = progression.replace(str(rand_elem), '..')
    print(f'Question: {progression}')


def is_correct_answer():
    correct_answer = str(random_answer)
    return correct_answer


def main():
    brain_games.scripts.engine.greet()
    brain_games.scripts.engine.ask_question(question)
    brain_games.scripts.engine.run_game(game_question, is_correct_answer)


if __name__ == '__main__':
    main()
