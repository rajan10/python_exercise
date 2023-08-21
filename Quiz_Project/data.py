# data.py
from question import Question

question_bank = [
    {"question": "Tradeau is the PM of Canada (True/False)", "answer": True},
    {"question": "Lalitpur is the capital of Nepal (True/False)", "answer": False},
    {"question": "Ottawa is the capital of Canada (True/False)", "answer": True},
    {"question": "Mt. Everest is in Nepal (True/False)", "answer": True},
    {"question": "The percentage of Oxygen in atmosphere is 30% (True/False)", "answer": True}
]

def get_question_bank():
    return [Question(q["question"], q["answer"]) for q in question_bank]
