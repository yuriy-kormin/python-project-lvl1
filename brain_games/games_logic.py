#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
ATTEMPTS = 3


def engine(game):
    '''
    engine to run game
    '''
    user = welcome_user()
    print(f"Hello, {user}!")
    print(game.get_rules())
    correct_answers = 0
    for attempt in range(ATTEMPTS):
        question, right_answer = game.get_question_answer()
        print(f'Question: {question}')
        answer = prompt.string(empty=True, prompt='Your answer: ')
        if str(answer) == str(right_answer):
            print("Correct!")
            correct_answers += 1
        else:
            result = f"'{answer}' is wrong answer ;(."
            result += f" Correct answer was '{right_answer}'."
            print(result)
            break
    if correct_answers == ATTEMPTS:
        print(f"Congratulations, {user}!")
    else:
        print(f"Let's try again, {user}!")
