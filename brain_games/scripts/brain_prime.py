#!/usr/bin/env python3
from brain_games.games.prime import prime, RULES_PRIME
from brain_games.games_logic import engine


def main():
    engine(prime, RULES_PRIME)


if __name__ == '__main__':
    main()
