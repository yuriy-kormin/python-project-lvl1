#!/usr/bin/env python3
from brain_games.games.calc import calc
from brain_games.scripts.games_logic import engine

def main():
    RULES = "What is the result of the expression?"
    engine(RULES, calc)


if __name__ == '__main__':
    main()
