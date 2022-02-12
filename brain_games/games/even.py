#!/usr/bin/env python3
from brain_games.scripts.games_logic import generate


def even():
    ''' Generate digit and calculate is it even '''
    [digit] = generate(1, 100)
    answer = "no" if digit % 2 else "yes"
    return [digit, answer]
