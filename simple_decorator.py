def add(a,b):
    return a+b

a=add #variable is used to point to function
print(a(2,3)) #function are first class object which means it can be passed as an argument


def hello_decorator(func):
    def inner():
        print("Hello, this is before function execution")
        func()
        print("This is after funtion execution")
    return inner


@hello_decorator
def function_to_be_used():
    print("This is inside the function")
    
#function_to_be_used=hello_decorator(function_to_be_used)
function_to_be_used()



def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument""")
    print(greeting)

greet(shout)
greet(whisper)
                    