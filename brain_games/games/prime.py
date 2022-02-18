from random import randint


RULES_PRIME = "Answer \"yes\" if given number is prime. "
RULES_PRIME += "Otherwise answer \"no\"."


def get_rules():
    return RULES_PRIME


def get_question_answer():
    ''' Generate digit and returm is it prime '''
    digit = randint(1, 50)
    answer = 'yes'
    if digit != 1:
        for i in range(2, digit):
            if not digit % i:
                answer = 'no'
    return digit, answer
