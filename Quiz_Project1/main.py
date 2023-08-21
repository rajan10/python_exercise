from data import get_object_from_dict
from quiz_controller import QuizController

def main():
    question_objects=get_object_from_dict()
    quiz=QuizController(question_objects)
    while quiz.has_next_question():
        quiz.next_question()
    
    
if __name__ == "__main__":
    main()