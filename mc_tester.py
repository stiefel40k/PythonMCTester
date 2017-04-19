#!/usr/bin/python3

import os.path
import sys
import json
import random

all_questions = 0
right_answers = 0
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
            all_questions += 1
            if right_answer == choice:
                right_answers += 1
                print('Your answer was right!')
            else:
                print('The right answer would have been: ' + right_answer +
                      ' your answer was: ' + choice)
            print()
    if all_questions > 0:
        print('You answered {0} questions correctly out of {1} questions.'.format(right_answers, all_questions))
        print('This means {0}%.'.format(right_answers/all_questions*100))
    print('Thanks for using this software. Bye')
    sys.exit(0)
