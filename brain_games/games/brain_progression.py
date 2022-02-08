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
    rules = "What number is missing in the progression?"
    qa = []
    for i in range(3):
        start = randint(1, 50)
        step = randint(1, 9)
        length = randint(5, 10)
        missing_pos = randint(0, length-1)
        if missing_pos == 0:
            q = ".."
        else:
            q = str(start)
        cur_val = start
        answer = start
        for i in range(1, length):
            cur_val += step
            if i == missing_pos:
                q += " " + ".."
                answer = cur_val
            else:
                q += " " + str(cur_val)
        qa.append([q, answer])
    logic(rules, qa)


if __name__ == '__main__':
    main()
