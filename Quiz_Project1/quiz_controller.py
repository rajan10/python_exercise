import sys
class QuizController:
    def __init__(self,object_list,score=0,question_number=0,play=True):
        self.object_list=object_list
        self.score=score
        self.question_number=question_number
        self.play=play
        self.total_question=len(object_list)
    
    def has_next_question(self)->bool:
        return self.question_number<self.total_question  
    
    def display_score(self):
        print(f"Your current score {self.score}/{self.total_question}")
        
    def check_answer_and_score(self, user_input, correct_answer):
        if user_input==correct_answer.lower():
            print("You got it right")
            self.score=self.score+1
        else:
            print("you got it Wrong")      
                  
    def play_again(self):
        play_input=input("Do you want to play again? (yes/no)").lower()
        if play_input=="yes":
            self.score=0
            self.question_number=0    
        elif play_input=="no":
            print("Thanks for playing!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'")
                                         
    def next_question(self):
        question_object=self.object_list[self.question_number]  
        user_input=input(f"{question_object.question}\nEnter your answer(True/False: )").lower()
        correct_answer=question_object.answer
        
        self.check_answer_and_score(user_input,correct_answer)

        self.display_score()   
        self.question_number=self.question_number+1
            
        if self.question_number==self.total_question:
            self.play_again()
        
