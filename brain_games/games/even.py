from random import randint


def get_rules():
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_answer():
    ''' Generate digit and calculate is it even '''
    question = randint(1, 100)
    answer = "no" if question % 2 else "yes"
    return str(question), answer
