#!/usr/bin/python3

import os.path
import sys
import json
import random


def print_question(questions):
    qn = random.randint(0, len(questions) - 1)
    question_text = questions[qn]['q']
    answer_text = ''
    for a in questions[qn]['answers']:
        answer_text += str(a['id']) + ') ' + a['text'] + '\n'
    print(question_text)
    print(answer_text)
    return questions[qn]['rightids']

if len(sys.argv) != 2:
    print('Usage: {0} <path_to_questions>'.format(sys.argv[0]))
    sys.exit(1)
else:
    with open(sys.argv[1], 'r') as f:
        questions = json.loads(f.read())
    # questions are read in. Inform the user about the usage:
    print('The questions are coming. If you want to quit, ' +
          'please hit q and Enter')
    print()
    print('Please enter the correct answers sorted as one number')
    print('So if you think answer 1, 2 and ' +
          '4 are the right one, please enter "124"')
    input('Press Enter to start')
    print()
    while True:
        right_answer = print_question(questions['questions'])
        choice = input(">>> ").lower().rstrip()
        if choice == 'q':
            break
        else:
            if right_answer == choice:
                print('Your answer was right!')
            else:
                print('The right answer would have been: ' + right_answer +
                      ' your answer was: ' + choice)
            print()
    print('Thanks for using this software. Bye')
    sys.exit(0)
