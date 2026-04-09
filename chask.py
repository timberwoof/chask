# chask.py
# asks you questions about your state of chastity
# calculates additional time for the chastity session
#
# Questions come from the accompanying chask.json file. 
# You may add questions
import random

questions = []
charges = []
answers = []
adds = []

platitudes = []

additional_time = 0
min_questions = 2
max_questions = 4
questions_to_ask = random.randint(min_questions, max_questions)
questions_asked = 0
charges_added = []

import json
with open('chask.json', 'r', encoding='utf-8') as questions_file:
    questions_obj = json.load(questions_file)

for platitude in questions_obj['platitudes']:
    platitudes.append(platitude)

for thing in questions_obj['questions']:
    questions.append(thing['question'])
    charges.append(thing['charge'])
    answers.append(thing['answer'])
    adds.append(thing['add'])

# set up the list of unasked questions
notasked = []
for i in range(0,len(questions)):
    notasked.append(i)

# print greeting
print('Thank you for coming to your appointment with the Chastity Compliance Review Board.')
print('I will ask you a series of questions. Answer truthfully with y for yes and n for no.')

while questions_asked < questions_to_ask:
    # pick a number frm the unasked questions
    question_number = random.randint(0, len(notasked)-1)

    # print the question
    print()
    print(f'{questions[notasked[question_number]]} [Y]')

    # get the answer, taunt the wearer, and calculate the added time
    answer = input().upper()
    if answer == 'Y':
        print(answers[notasked[question_number]])
        additional_time = additional_time + adds[notasked[question_number]]
        charges_added.append([ charges[notasked[question_number]], adds[notasked[question_number]] ])

    # remove the question from the list of qunasked uestions
    notasked.pop(question_number)

    questions_asked = questions_asked + 1

print()
print('Thank you for answering the questions.')
print()

print('Here is your chastity compliance report:')
print('=============================================')
print('Chastity Compliance Report and Recommendation')
print()
if len(charges_added) > 0:
    print('Subject reported the following compliance problems.')
    print('Each is presented with its associated penalty:')
    for charge in charges_added:
        print(f'{charge[0]}: {charge[1]}')
    print();
    print('Chastity Review Officer Recommendation:')
    plural = ''
    if additional_time > 1:
        plural = 's'
    print(f"Subject is to add {additional_time} hour{plural} to his time.")
else:
    print('Subject reported no compliance problems.')
    print('No penalty is recommended at this time.')
    print('Subject must continue to obey chastity.')

print('=============================================')
print(f'You may go. Remember, {platitudes[random.randint(0,len(platitudes)-1)]}')


