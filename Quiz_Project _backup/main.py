from data import question_bank
from question_model import Question

questions= []
def create_question_object(question_dict: dict)->Question:   #pass dict to create object 
    return Question(question=question_dict["question"], answer=question_dict["answer"])  #object creation of dict

for question in question_bank:
    question_object=create_question_object(question_dict=question)
    questions.append(question_object)
    
 
while True:  
    for question in questions:
        print(question)
        user_input = input("Please enter your answer (True/False): ")
        user_answer = user_input.lower() == "true"
