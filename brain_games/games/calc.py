#!/usr/bin/env python3
from brain_games.scripts.games_logic import generate


def calc():
    ''' Generate math expression and calculate it '''
    operation = ["+", "-", "*"]
    [digit1, digit2] = generate(2, 20)
    [operation_type] = generate(1, 2)
    question = f"{digit1} {operation[operation_type]} {digit2}"
    return [question, eval(question)]
