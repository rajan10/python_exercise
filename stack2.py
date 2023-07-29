class Stack:
    def __init__(self):
        self.container=[]
        
    def is_empty(self):
        if len(self.container)==0:
           return True
        else: 
            return False
    
    def push(self,element):
        self.container.append(element)
        print(f"{element} is pushed")
    
    def pop(self):
        if self.is_empty():
            print("list is empty")
        else:
            removed_element=self.container.pop()
            return removed_element
    
    def display(self):
        if self.is_empty():
            print("No elements in the Stack")
        else: 
            for element in self.container:
                print(element)
                
my_stack= Stack()
my_stack.push(1)
#my_stack.push(2)
my_stack.pop()
my_stack.pop()
my_stack.display()