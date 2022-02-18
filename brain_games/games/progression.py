from random import randint, choice


RULES_PROGRESSION = "What number is missing in the progression?"


def get_rules():
    return RULES_PROGRESSION


def get_question_answer():
    '''Generate arithmetic progression with missing member'''
    start_digit = randint(2, 9)
    step = randint(2, 9)
    length = randint(5, 10)
    end_digit = start_digit + (step - 1) * length + 1
    progression = [i for i in (range(start_digit, end_digit, step))]
    missing_member_index = progression.index(choice(progression))
    answer = str(progression[missing_member_index])
    progression[missing_member_index] = '..'
    question = " ".join([str(elem) for elem in progression])
    # if missing_position == 0:
    #     question = ".."
    #     answer = start_digit
    # else:
    #     question = str(start_digit)
    # current_value = start_digit
    # for i in range(1, length):
    #     current_value += step
    #     if i == missing_position:
    #         question += " " + ".."
    #         answer = current_value
    #     else:
    #         question += " " + str(current_value)
    return question, answer
