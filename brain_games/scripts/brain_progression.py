#!/usr/bin/env python3
from brain_games.games.progression import get_progression, RULES_PROGRESSION
from brain_games.games_logic import engine


def main():
    engine(get_progression, RULES_PROGRESSION)


if __name__ == '__main__':
    main()
