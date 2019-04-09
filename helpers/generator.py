import os.path
import json
import random

class Generator:
	def get_difficulty_ratios(self):
		with open(os.path.dirname(__file__) + '/../config/ratios.json') as json_file:
			ratios = json.load(json_file)
		return ratios


	def pick_questions(self, required_total_marks, json_file_path):	
		selected_questions = []
		marks_left = 0;
		with open(json_file_path) as json_file:  
			all_questions = json.load(json_file)
			total_marks = 0

			while total_marks < required_total_marks :
				question = random.choice(all_questions)
				if question not in selected_questions:
					selected_questions.append(question)
					total_marks += question['marks'];

			if total_marks > required_total_marks:
				total_marks -= selected_questions[-1]['marks']
				selected_questions = selected_questions[:-1]
				marks_left = required_total_marks - total_marks
				
				for question in all_questions:
					if question['marks'] == marks_left and question not in selected_questions:
						selected_questions.append(question)
						total_marks+=question['marks']
						marks_left = 0;
						break


		picked_data = {
			'questions':selected_questions,
			'total_marks_picked':total_marks,
			'required_marks':required_total_marks,
			'marks_left':marks_left
		}

		return picked_data
