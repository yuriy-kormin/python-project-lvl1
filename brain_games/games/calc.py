#!/usr/bin/env python3
from random import randint, choice
import operator


RULES_CALC = 'What is the result of the expression?'


def calc():
    ''' Generate math expression and calculate it '''
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operand_left = randint(1, 10)
    operand_right = randint(1, 10)
    operation = choice(list(operations.keys()))

    question = f"{operand_left} {operation} {operand_right}"
    answer = operations[operation](operand_left, operand_right)
    return question, answer
