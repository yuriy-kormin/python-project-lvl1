#!/usr/bin/env python3
from brain_games.games.prime import get_prime, RULES_PRIME
from brain_games.games_logic import engine


def main():
    engine(get_prime, RULES_PRIME)


if __name__ == '__main__':
    main()
