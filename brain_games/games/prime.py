from random import randint


def get_rules():
    return "Answer \"yes\" if given number is prime. \
Otherwise answer \"no\"."


def is_prime(digit):
    ''' check is digit prime'''
    if digit < 2:
        return False
    else:
        for i in range(2, digit // 2 + 1):
            if not digit % i:
                return False
    return True


def get_question_answer():
    ''' Generate digit and returm is it prime '''
    question = randint(1, 50)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
