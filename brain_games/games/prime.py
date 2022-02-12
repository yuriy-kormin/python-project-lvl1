#!/usr/bin/env python3
from brain_games.scripts.games_logic import generate


def is_prime(number):
    ''' Check number is prime '''
    for i in range(2, number):
        if not number % i:
            return "no"
    return "yes"


def prime():
    ''' Generate digit and returm is it prime '''
    [digit] = generate(1, 50)
    return [digit, is_prime(digit)]
