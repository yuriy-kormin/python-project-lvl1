#!/usr/bin/env python3
from brain_games.games.prime import prime
from brain_games.scripts.games_logic import engine


def main():
    RULES = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
    engine(RULES, prime)


if __name__ == '__main__':
    main()
