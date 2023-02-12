#!/usr/bin/env python3
import brain_games.scripts.engine
import random


question = 'What number is missing in the progression?'
def game_question():
    global l
    progression_step = random.randint(1, 5)
    progression_length = random.randint(5, 10)
    l = []
    first_elem = random.randint(1, 50)
    l.append(first_elem)
    counter = 0
    while counter < progression_length - 1:
        l.append(l[counter] + progression_step)
        counter += 1
    rand_elem = random.choice(l)
    global random_answer
    random_answer = rand_elem
    l = str(l)
    l = l.replace(str(rand_elem), '..')
    print(f'Question: {l}')


def is_correct_answer():
    correct_answer = str(random_answer)
    return correct_answer

def main():
    brain_games.scripts.engine.greet()
    brain_games.scripts.engine.ask_question(question)
    brain_games.scripts.engine.run_game(game_question, is_correct_answer)

if __name__ == '__main__':
    main()
