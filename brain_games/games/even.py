#!/usr/bin/env python3
from random import randint


RULES_EVEN = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def even():
    ''' Generate digit and calculate is it even '''
    digit = randint(1, 100)
    answer = "no" if digit % 2 else "yes"
    return digit, answer
