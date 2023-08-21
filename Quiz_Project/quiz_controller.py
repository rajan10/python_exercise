# quiz_controller.py
from question import Question

class QuizController:
    def __init__(self, question_list):
        self.score = 0
        self.question_list = question_list
        self.question_number = 0
       

    def check_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer.lower()

    def next_question(self):
        if self.has_next_question():
            self.question_number += 1

    def has_next_question(self):
        return self.question_number < len(self.question_list)

    def display_score(self):
        print(f"Your current score is: {self.score}/{len(self.question_list)}")

   
        