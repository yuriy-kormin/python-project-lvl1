#!/usr/bin/env python3
from random import randint


RULES_PROGRESSION = "What number is missing in the progression?"


def progression():
    '''Generate arithmetic progression with missng member'''
    start_digit = randint(2, 9)
    step = randint(2, 9)
    length = randint(5, 10)
    missing_position = randint(0, length - 1)
    if missing_position == 0:
        question = ".."
        answer = start_digit
    else:
        question = str(start_digit)
    current_value = start_digit
    for i in range(1, length):
        current_value += step
        if i == missing_position:
            question += " " + ".."
            answer = current_value
        else:
            question += " " + str(current_value)
    return question, answer
