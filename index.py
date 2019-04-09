from helpers.generator import Generator
import json
import random

while True:
	try:
		total_number_of_marks = int(input("Enter number of total marks : ")); 
	except ValueError:
		print("That's not an int!")
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
	print("\nCan't reach required marks for Easy Section, add a question for %d marks" % selected_easy_questions['marks_left'])
if(selected_medium_questions['total_marks_picked'] != marks_of_medium_questions):
	print("\nCan't reach required marks for Medium Section, add a question for %d marks" % selected_medium_questions['marks_left'])
if(selected_hard_questions['total_marks_picked'] != marks_of_hard_questions):
	print("\nCan't reach required marks for Hard Section, add a question for %d marks" % selected_hard_questions['marks_left'])

print("\nEasy Section : %d" % selected_easy_questions['total_marks_picked'])
for question in selected_easy_questions['questions']:
	print("Question ID : %d , Marks : %d" % (question['id'], question['marks']))

print("\nMedium Section : %d" % selected_medium_questions['total_marks_picked'])
for question in selected_medium_questions['questions']:
	print("Question ID : %d , Marks : %d" % (question['id'], question['marks']))

print("\nHard Section : %d" % selected_hard_questions['total_marks_picked'])
for question in selected_hard_questions['questions']:
	print("Question ID : %d , Marks : %d" % (question['id'], question['marks']))

# selected_easy_questions = []

# with open('questions_db/easy/questions.json') as json_file:  
# 	all_easy_questions = json.load(json_file)

# 	total_marks = 0
# 	while total_marks < marks_of_easy_questions :
# 		single_question = random.choice(all_easy_questions)
# 		if single_question not in selected_easy_questions:
# 			selected_easy_questions.append(single_question)
# 			total_marks += single_question['marks'];

# 	if total_marks > marks_of_easy_questions:
# 		total_marks -= selected_easy_questions[-1]['marks']
# 		selected_easy_questions = selected_easy_questions[:-1]
# 		marks_left = marks_of_easy_questions - total_marks
# 		print("Left marks : %d" % marks_left)
# 		for question in all_easy_questions:
# 			print(question['marks'] == marks_left) 
# 			print("ID %d" % question['question_id'])
# 			if question['marks'] == marks_left and question not in selected_easy_questions:
# 				selected_easy_questions.append(question)
# 				total_marks+=question['marks']
# 				break
	
# 	print("Total Marks : %d" % total_marks)
# 	print("Easy questions Ready!")

# 	for question in selected_easy_questions:
# 		print("Question ID: %d" % question['question_id'])
# 		print("Marks: %d" % question['marks'])

	# for question in selected_easy_questions:
	# 	print("Question Id : %d" % question['question_id'])
	# 	print("Marks : %d" % question['marks'])
		
	# print(total_marks)
# with open('questions_db/medium/questions.json') as json_file:  
#     all_medium_questions = json.load(json_file)
#     for x in all_medium_questions:
#         print(x['marks'])
#         print(x['question_id'])


# with open('questions_db/hard/questions.json') as json_file:  
#     all_hard_questions = json.load(json_file)
#     for x in all_hard_questions:
#         print(x['marks'])
#         print(x['question_id'])