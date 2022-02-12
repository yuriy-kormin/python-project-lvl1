#!/usr/bin/env python3
from random import randint


def nod(a, b):
    '''
    Find greatest common divisor of two digits
    '''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcd():
    '''
    Generate 2 digits and return greatest common divisor of it
    '''
    digit1 = randint(1, 50)
    digit2 = randint(2, 50)
    return ([f'{digit1} {digit2}', nod(digit1, digit2)])
