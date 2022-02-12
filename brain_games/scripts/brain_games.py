#!/usr/bin/env python3
from brain_games.scripts.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Hello, %s!" % name)


if __name__ == '__main__':
    main()