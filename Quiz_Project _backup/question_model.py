class Question:
    def __init__(self, question: str, answer:bool)->None:
        self.question =question
        self.answer=answer
        
    def __repr__(self):
        return f"<Question: {self.question}:{self.answer}>"
        
    def check_answer(self, user_answer, correct_answer) -> bool:
        return user_answer == correct_answer