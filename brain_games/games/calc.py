#!/usr/bin/env python3
from random import randint


def calc():
    ''' Generate math expression and calculate it '''
    operation = ["+", "-", "*"]
    operation_type = randint(0, 2)
    digit1 = randint(1, 20)
    digit2 = randint(1, 20)
    question = f"{digit1} {operation[operation_type]} {digit2}"
    return [question, eval(question)]
