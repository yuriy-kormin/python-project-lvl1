#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games_logic import logic


def main():
    rules = "What is the result of the expression?"
    qa = []
    operation = ["+", "-", "*"]
    for i in range(3):
        operation_type = randint(0, 2)
        digit1 = randint(1, 20)
        digit2 = randint(1, 20)
        if operation_type == 2:
            digit2 = randint(1, 5)
            answer = digit1 * digit2
        elif operation_type == 1:
            answer = digit1 - digit2
        else:
            answer = digit1 + digit2
        qa.append([f'{digit1} {operation[operation_type]} {digit2}', answer])
    logic(rules, qa)


if __name__ == '__main__':
    main()
