#!/usr/bin/env python3
import prompt


def welcome_user():
    return prompt.string(empty=False, prompt='May I have your name? ')
