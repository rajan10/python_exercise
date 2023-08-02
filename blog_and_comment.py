class Blog:
    def __init__(self, title, content):
        self.title=title
        self.content= content
        self.comment=None
       
    def add_comment(self,comment):
        if not self.comment:
            self.comment= comment
            return comment
        else:
            print("Already commmented")
            
    def __str__(self):
        return f" {self.title}-- {self.content} --{self.comment}"
             
    
class Comment:
    def __init__(self, comment):
        
        self.comment=comment
        
my_blog=Blog(" My Travel Blog", "This is my travel blog....")  
print(my_blog)   
print(my_blog.add_comment("Nice blog.This is my first comment"))
print(my_blog) 
my_blog.add_comment("updated comment")
my_blog.add_comment("updated comment")
my_blog.comment="This is my udpated comment"
print(my_blog)
print(f" Title ={my_blog.title}, Content = {my_blog.content} Comment = {my_blog.comment}")


