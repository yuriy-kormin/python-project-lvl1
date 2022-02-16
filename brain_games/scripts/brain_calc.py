#!/usr/bin/env python3
from brain_games.games.calc import calc, RULES_CALC
from brain_games.games_logic import engine


def main():
    engine(calc, RULES_CALC)


if __name__ == '__main__':
    main()
