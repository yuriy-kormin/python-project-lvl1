#!/usr/bin/env python3
from brain_games.games.gcd import gcd, RULES_GCD
from brain_games.games_logic import engine


def main():
    engine(gcd, RULES_GCD)


if __name__ == '__main__':
    main()
