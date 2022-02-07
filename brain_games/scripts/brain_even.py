#!/usr/bin/env python3
from random import randint
from brain_games.scripts.cli import welcome_user
import prompt


def main():
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    test_num = 3
    test = 1
    correct_answers = 0
    while test <= test_num:
        digit = randint(1, 100)
        # print (f'correct answers {correct_answers}')
        print("Question: " + str(digit))
        answer = prompt.string(empty=True, prompt='Your answer: ')
        if(
            (digit % 2 and answer == "no") or
            (not(digit % 2) and answer == "yes")
          ):
            print("Correct!")
            test += 1
            correct_answers += 1
            continue
        elif digit % 2:
            right_answer = 'no'
        else:
            right_answer = 'yes'
        print("'%s' is wrong answer ;(. Correct answer was '%s'."
              % (answer, right_answer))
        break
    if correct_answers == test_num:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
