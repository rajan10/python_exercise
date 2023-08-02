class Book:
    def __init__(self,name, author, publisher):
        self.name=name
        self.author =author
        self.publisher= publisher
        
    def display_author_name(self):
        return self.author.name
        
class Author:
    def __init__(self, name, gender, dob):
        self.name=name
        self.gender=gender
        self.dob =dob

valmiki=Author("VALMIKI","male","2066/12/15")
ramayan=Book("The Ramayan",valmiki,"Image Publisher")
print(ramayan.display_author_name())



