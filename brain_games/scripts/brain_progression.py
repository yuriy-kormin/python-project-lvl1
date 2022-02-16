#!/usr/bin/env python3
from brain_games.games.progression import progression, RULES_PROGRESSION
from brain_games.games_logic import engine


def main():
    engine(progression, RULES_PROGRESSION)


if __name__ == '__main__':
    main()
