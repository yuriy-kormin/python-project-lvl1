from random import randint, choice
import operator


def get_rules():
    return 'What is the result of the expression?'


def get_question_answer():
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
    return question, str(answer)
