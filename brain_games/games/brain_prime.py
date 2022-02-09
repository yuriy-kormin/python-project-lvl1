#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games_logic import logic


def is_prime(a):
    for i in range(2, a):
        if not a % i:
            return "no"
    return "yes"


def main():
    rules = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
    qa = []
    for i in range(3):
        digit = randint(1, 50)
        qa.append([digit, is_prime(digit)])
    logic(rules, qa)


if __name__ == '__main__':
    main()
