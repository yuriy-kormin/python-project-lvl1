from random import randint, choice


Description = "What number is missing in the progression?"


def get_question_answer():
    '''Generate arithmetic progression with missing member'''
    start_digit = randint(2, 9)
    step = randint(2, 9)
    length = randint(5, 10)
    end_digit = start_digit + (length - 1) * step + 1
    progression = list(range(start_digit, end_digit, step))
    missing_member_index = progression.index(choice(progression))
    answer = progression[missing_member_index]
    progression[missing_member_index] = '..'
    question = " ".join([str(elem) for elem in progression])
    return question, str(answer)
