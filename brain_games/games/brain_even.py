#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games_logic import logic


def main():
    rules = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    qa = []
    for i in range(3):
        digit = randint(1, 100)
        answer = "no" if digit % 2 else "yes"
        qa.append([digit, answer])
    logic(rules, qa)


if __name__ == '__main__':
    main()
