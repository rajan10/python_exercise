class Book:
    def __init__(self, name,author,publisher,price):
        self.name= name
        self.author=author
        self.publisher=publisher
        self.price=price   
    def __str__(self):    
        return f"Book:{self.name}"
    
    def get_author(self):
        return self.author.name
        
class Author:
    def __init__(self,name,gender,nationality,dob):
        self.name=name
        self.gender=gender   
        self.nationality=nationality
        self.dob=dob
    def __str__(self):
        return f"Author: {self.name}"

    def hello(self):
        return "hello World"
        
ram= Author("Ram Prasad", "Male","Nepali", "2055/12/15")

print(ram)   
print(ram.name)   
jungle_book= Book("The Jungle Book", ram,"Image Publication",500)
print(jungle_book)
print(jungle_book.get_author())
print(ram.hello())


