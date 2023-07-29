class Stack:
    def __init__(self):
        self.container=[]
        
    def push(self,element):
        self.container.append(element)
        print(f"{element} has been pushed in the list")

    def pop(self):
        # check if empty
        removed_element=self.container.pop()
        return removed_element
        
    def display(self):
        for element in self.container:
            print(element)   
            ## check if list is empty or not

# create fun is_empty

# def size of list 
my_stack= Stack()
my_stack.push(1)
my_stack.pop()
my_stack.display()