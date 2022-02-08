#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games_logic import logic


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


def main():
    rules = "Find the greatest common divisor of given numbers."
    qa = []
    for i in range(3):
        digit1 = randint(1, 50)
        digit2 = randint(2, 50)
        qa.append([f'{digit1} {digit2}', nod(digit1, digit2)])
    logic(rules, qa)


if __name__ == '__main__':
    main()
