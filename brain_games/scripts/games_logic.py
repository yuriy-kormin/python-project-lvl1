#!/usr/bin/env python3
import prompt
from brain_games.scripts.cli import welcome_user


def ask_question(question):
    print("Question: " + str(question))
    return prompt.string(empty=True, prompt='Your answer: ')

def fill_question_array(logic_function,attempts=3):
    question_answer=[]
    for i in range(attempts):
        question_answer.append(logic_function())
    return question_answer

def engine(rules, function):
    '''
        rules - string to show user to explain game rules
        qa: list questions-answers. format is [[q1,a1],[q2,a2]...]
        attempts - int How many times we need to ask user

    '''
    # print (qa)
    questions_answers=fill_question_array(function)
    user = welcome_user()
    print(f"Hello, {user}!")
    print(rules)
    correct_answers = 0
    for question in questions_answers:
        answer = ask_question(question[0])
        if str(answer) == str(question[1]):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{question[1]}'.")
            break
    if correct_answers == len(questions_answers):
        print(f"Congratulations, {user}!")
    else:
        print(f"Let's try again, {user}!")


def main():
    pass


if __name__ == "__main__":
    main()
