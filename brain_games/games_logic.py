import prompt
from brain_games.cli import welcome_user
ATTEMPTS = 3


def engine(function, rules):
    '''
        rules - string to show user to explain game rules
        function - name of def, which make logic of game
    '''
    user = welcome_user()
    print(f"Hello, {user}!")
    print(rules)
    correct_answers = 0
    attempt = 1
    while attempt <= ATTEMPTS:
        question, right_answer = function()
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
        attempt += 1
    if correct_answers == ATTEMPTS:
        print(f"Congratulations, {user}!")
    else:
        print(f"Let's try again, {user}!")
