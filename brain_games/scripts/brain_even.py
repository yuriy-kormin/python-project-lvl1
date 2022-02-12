#!/usr/bin/env python3
from brain_games.games.even import even
from brain_games.scripts.games_logic import engine


def main():
    RULES = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    engine(RULES, even)


if __name__ == '__main__':
    main()
