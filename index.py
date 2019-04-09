from helpers.generator import Generator
import json
import random

while True:
	try:
		total_number_of_marks = int(input("Enter number of total marks : ")); 
	except ValueError:
		print("That's not an int!")
		continue
	if total_number_of_marks < 10 :
		print("\n Oh! Error! - Please insert a value between 10 and 100")
		continue
	else:
		break


paper_generator = Generator()

ratios = paper_generator.get_difficulty_ratios()

marks_of_easy_questions = round(ratios['easy'] * total_number_of_marks)

marks_of_medium_questions = round(ratios['medium'] * total_number_of_marks)

marks_of_hard_questions = round(ratios['hard'] * total_number_of_marks)

print("\nTotal Number of Marks : %d" % total_number_of_marks)

print("\nRequired Marks ---- ")
print("Easy : %d" % marks_of_easy_questions)
print("Medium : %d" % marks_of_medium_questions)
print("Hard : %d" % marks_of_hard_questions)

selected_easy_questions = paper_generator.pick_questions(marks_of_easy_questions, 'questions_db/easy/questions.json')
selected_medium_questions = paper_generator.pick_questions(marks_of_medium_questions, 'questions_db/medium/questions.json')
selected_hard_questions = paper_generator.pick_questions(marks_of_hard_questions, 'questions_db/hard/questions.json')

if(selected_easy_questions['total_marks_picked'] != marks_of_easy_questions):
	print("\nCan't reach required marks for Easy Section, please add a question for %d marks in data" % selected_easy_questions['marks_left'])
print("Easy Section : %d" % selected_easy_questions['total_marks_picked'])
for question in selected_easy_questions['questions']:
	print("Question ID : %d , Marks : %d" % (question['id'], question['marks']))

if(selected_medium_questions['total_marks_picked'] != marks_of_medium_questions):
	print("\nCan't reach required marks for Medium Section, please add a question for %d marks in data" % selected_medium_questions['marks_left'])
print("Medium Section : %d" % selected_medium_questions['total_marks_picked'])
for question in selected_medium_questions['questions']:
	print("Question ID : %d , Marks : %d" % (question['id'], question['marks']))

if(selected_hard_questions['total_marks_picked'] != marks_of_hard_questions):
	print("\nCan't reach required marks for Hard Section, please add a question for %d marks in data" % selected_hard_questions['marks_left'])
print("Hard Section : %d" % selected_hard_questions['total_marks_picked'])
for question in selected_hard_questions['questions']:
	print("Question ID : %d , Marks : %d" % (question['id'], question['marks']))
