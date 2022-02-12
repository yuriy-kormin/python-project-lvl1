#!/usr/bin/env python3
from random import randint


def even():
    ''' 
    Generate digit and calculate is it even
    '''
    digit = randint(1, 100)
    answer = "no" if digit % 2 else "yes"
    return [digit, answer]
