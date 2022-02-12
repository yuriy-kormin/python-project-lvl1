#!/usr/bin/env python3
from brain_games.scripts.games_logic import generate


def progression():
    '''Generate arithmetic progression with missng member'''
    [start, step] = generate(2, 9)
    [length] = generate(1, 10, 5)
    [missing_pos] = generate(1, length - 1)
    if missing_pos == 0:
        question = ".."
    else:
        question = str(start)
    cur_val = start
    answer = start
    for i in range(1, length):
        cur_val += step
        if i == missing_pos:
            question += " " + ".."
            answer = cur_val
        else:
            question += " " + str(cur_val)
    return [question, answer]
