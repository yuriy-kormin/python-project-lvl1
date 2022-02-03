#!/usr/bin/env python3
from cli import welcome_user as welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Hello, %s!" % name)


if __name__ == '__main__':
    main()
