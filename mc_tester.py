#!/usr/bin/python3

import os.path
import sys
import json
import random
import re

all_questions = 0
right_answers = 0
used_questions = []
def print_question(questions):
    # check if there is any more questions if not return None
    if len(used_questions) == len(questions):
        print('The questionpool has been emtied. No more questions.')
        return None
    
    # choose a random question, if it was already used take another one
    qn = random.randint(0, len(questions) - 1)
    while qn in used_questions:
        qn = random.randint(0, len(questions) - 1)
    used_questions.append(qn)

    # format the question text to add some numbering
    question_text = '{0}/{1}) {2}'.format(str(len(used_questions)), str(len(questions)), questions[qn]['q'])
    answer_text = ''
    counter = 1
    new_rightids = ''
    # randomize and print the answers
    answers = questions[qn]['answers']
    random.shuffle(answers)
    for a in answers:
        if str(a['id']) in questions[qn]['rightids']:
            # remap the right id-s according to the new index after the randomization
            new_rightids += str(counter)
        answer_text += str(counter) + ') ' + a['text'] + '\n'
        counter += 1
    print(question_text)
    print(answer_text)
    return new_rightids

if len(sys.argv) != 2:
    # print usage if no path is given
    print('Usage: {0} <path_to_questions>'.format(sys.argv[0]))
    sys.exit(1)
else:
    with open(sys.argv[1], 'r') as f:
        questions = json.loads(f.read())
    # questions are read in. Inform the user about the usage
    print('The questions are coming. If you want to quit, ' +
          'please hit q and Enter')
    print()
    print('You can enter the answers in any kind of form.')
    print('So if you think answer 1, 2 and ' +
          '4 are the right one, you can enter "1 2 4" or "241" ' +
          'or anything else.')
    input('Press Enter to start')
    print()
    while True:
        right_answer = print_question(questions['questions'])
        if right_answer is None:
            # there is no more questions exiting
            break
        choice = input(">>> ").lower().rstrip()
        if choice == 'q':
            # user input to exit
            break
        else:
            # process user input and compare to the right id-s
            all_questions += 1
            choice = re.findall('[1-9]', choice)
            choice.sort()
            choice = ''.join(choice)
            if right_answer == choice:
                right_answers += 1
                print('Your answer was right!')
            else:
                print('The right answer would have been: ' + right_answer +
                      ' your answer was: ' + choice)
            print()
    if all_questions > 0:
        # print some statistics
        print('You answered {0} questions correctly out of {1} questions.'.format(right_answers, all_questions))
        print('This means {0}%.'.format(right_answers/all_questions*100))
    print('Thanks for using this software. Bye')
    sys.exit(0)
