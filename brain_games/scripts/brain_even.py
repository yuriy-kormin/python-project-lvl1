#!/usr/bin/env python3
from brain_games.games.even import even, RULES
from brain_games.games_logic import engine


def main():
    engine(even, RULES)


if __name__ == '__main__':
    main()
