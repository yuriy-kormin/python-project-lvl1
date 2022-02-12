#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.scripts.games_logic import engine

def main():
    RULES = "Find the greatest common divisor of given numbers."
    engine(RULES, gcd)


if __name__ == '__main__':
    main()
