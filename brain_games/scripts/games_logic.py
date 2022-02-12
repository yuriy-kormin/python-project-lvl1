#!/usr/bin/env python3
import prompt
from brain_games.scripts.cli import welcome_user


def ask_question(question):
    print("Question: " + str(question))
    return prompt.string(empty=True, prompt='Your answer: ')


def fill_question_array(logic_function, attempts=3):
    question_answer = []
    for i in range(attempts):
        question_answer.append(logic_function())
    return question_answer


def engine(rules, function):
    '''
        rules - string to show user to explain game rules
        function - name of def, which make logic of game
    '''
    questions_answers = fill_question_array(function)
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
            result = f"'{answer}' is wrong answer ;(."
            result += f" Correct answer was '{question[1]}'."
            print(result)
            break
    if correct_answers == len(questions_answers):
        print(f"Congratulations, {user}!")
    else:
        print(f"Let's try again, {user}!")


def main():
    pass


if __name__ == "__main__":
    main()
