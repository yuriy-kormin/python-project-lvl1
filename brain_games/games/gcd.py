from random import randint


Description = "Find the greatest common divisor of given numbers."


def get_gcd(operand_left, operand_right):
    '''find greatest common divisor of 2 digits'''
    while operand_left != 0 and operand_right != 0:
        if operand_left > operand_right:
            operand_left = operand_left % operand_right
        else:
            operand_right = operand_right % operand_left
    return operand_left + operand_right


def get_question_answer():
    ''' Generate 2 digits and return greatest common divisor of it '''
    operand_left = randint(1, 50)
    operand_right = randint(1, 50)
    question = f'{operand_left} {operand_right}'
    answer = get_gcd(operand_left, operand_right)
    return question, str(answer)
