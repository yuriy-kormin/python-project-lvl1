#!/usr/bin/env python3
from brain_games.scripts.games_logic import generate


def nod(a, b):
    ''' Find greatest common divisor of two digits '''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcd():
    ''' Generate 2 digits and return greatest common divisor of it '''
    [digit1, digit2] = generate(2, 50)
    return ([f'{digit1} {digit2}', nod(digit1, digit2)])
