#!/usr/bin/env python3
from brain_games.games.progression import progression
from brain_games.scripts.games_logic import engine


def main():
    RULES = "What number is missing in the progression?"
    engine(RULES, progression)


if __name__ == '__main__':
    main()
