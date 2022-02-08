#!/usr/bin/env python3
import prompt
from brain_games.scripts.cli import welcome_user


def question(q):
    print("Question: " + str(q))
    return prompt.string(empty=True, prompt='Your answer: ')


def logic(rules, qa):
    '''
        rules - string to show user to explain game rules
        qa: list questions-answers. format is [[q1,a1],[q2,a2]...]
        attempts - int How many times we need to ask user

    '''
    # print (qa)
    user = welcome_user()
    print(f"Hello, {user}!")
    correct_answers = 0
    for q in qa:
        answer = question(q[0])
        if str(answer) == str(q[1]):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{q[1]}'.")
            break
    if correct_answers == len(qa):
        print(f"Congratulations, {user}!")
    else:
        print(f"Let's try again, {user}!")


def main():
    pass


if __name__ == "__main__":
    main()
