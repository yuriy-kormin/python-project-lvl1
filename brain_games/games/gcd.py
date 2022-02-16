#!/usr/bin/env python3
from random import randint


RULES_GCD = "Find the greatest common divisor of given numbers."


def get_gcd():
    ''' Generate 2 digits and return greatest common divisor of it '''
    operand_left = randint(1, 50)
    operand_right = randint(1, 50)
    question = f'{operand_left} {operand_right}'
    while operand_left != 0 and operand_right != 0:
        if operand_left > operand_right:
            operand_left = operand_left % operand_right
        else:
            operand_right = operand_right % operand_left
    answer = operand_left + operand_right
    return question, answer
