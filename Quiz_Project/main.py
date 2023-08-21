# main.py
from data import get_question_bank
from quiz_controller import QuizController

def main():
    questions = get_question_bank()
    quiz = QuizController(questions)  
    # question_objects is passed as an argume

    while quiz.has_next_question():
        question = quiz.question_list[quiz.question_number]
        print(question.question)
        
        user_input = input("Please enter your answer (True/False): ").lower()
        user_answer = user_input == "true"
        correct_answer = question.answer

        if quiz.check_answer(user_answer, correct_answer):
            print("You got it right!")
            quiz.score += 1
        else:
            print("You got it wrong!")

        quiz.next_question()
        quiz.display_score()

if __name__ == "__main__":
    main()
