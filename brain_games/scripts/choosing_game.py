#!/usr/bin/env python3
from brain_games.games import calc, even, gcd, prime, progression
from brain_games.engine import run_game

VARIANTS = {"1": calc,
            "2": even,
            "3": gcd,
            "4": prime,
            "5": progression}


def main():
    option = ''
    while option != "0":
        print('\nPlease, choose your game:')
        for i in VARIANTS:
            print(f'  [{i}]: {VARIANTS[i].Description}')
        print("  [0]: exit")
        option = input()
        if option == 0:
            break
        elif option in VARIANTS:
            run_game(VARIANTS[option])


if __name__ == '__main__':
    main()
