#!/usr/bin/env python3
from brain_games.games.gcd import get_gcd, RULES_GCD
from brain_games.games_logic import engine


def main():
    engine(get_gcd, RULES_GCD)


if __name__ == '__main__':
    main()
