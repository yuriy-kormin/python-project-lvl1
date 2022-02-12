#!/usr/bin/env python3
from random import randint


def progression():
    '''
    Generate arithmetic progression with missng member
    '''
    start = randint(1, 50)
    step = randint(1, 9)
    length = randint(5, 10)
    missing_pos = randint(0, length - 1)
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
    return[question, answer]
