#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user


def run_game(game):
    '''
    engine to run game
    '''
    game_rounds_count = 3
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    print(game.get_rules())
    for attempt in range(game_rounds_count):
        question, right_answer = game.get_question_answer()
        print(f'Question: {question}')
        answer = prompt.string(empty=True, prompt='Your answer: ')
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return False
        print("Correct!")
    print(f"Congratulations, {user_name}!")
