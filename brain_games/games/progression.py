from random import randint, choice


RULES_PROGRESSION = "What number is missing in the progression?"


def get_rules():
    return RULES_PROGRESSION


def get_question_answer():
    '''Generate arithmetic progression with missing member'''
    start_digit = randint(2, 9)
    step = randint(1, 9)
    length = randint(5, 10)
    end_digit = start_digit + step * (length - 1)
    progression = [i for i in (range(start_digit, end_digit + 1, step))]
    missing_member = choice(progression)
    missing_member_index = progression.index(missing_member)
    progression[missing_member_index] = '..'
    answer = missing_member
    question = " ".join([str(elem) for elem in progression])
    return question, answer
