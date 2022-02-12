#!/usr/bin/env python3
from random import randint


def is_prime(number):
    ''' Check number is prime '''
    for i in range(2, number):
        if not number % i:
            return "no"
    return "yes"


def prime():
    ''' Generate digit and returm is it prime '''
    digit = randint(1, 50)
    return [digit, is_prime(digit)]



