#!/usr/bin/env python3
from brain_games.games.even import get_even, RULES_EVEN
from brain_games.games_logic import engine


def main():
    engine(get_even, RULES_EVEN)


if __name__ == '__main__':
    main()
