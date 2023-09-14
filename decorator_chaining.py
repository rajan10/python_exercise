

def middle(func):
    def wrapper(*args, **kwargs):
        print("2" * 2)
        func(*args, **kwargs)
        print("2" * 2)
    return wrapper

def bottom(func):
    def wrapper(*args, **kwargs):
        print("3" * 3)
        func(*args, **kwargs)
        print("3" * 3)
    return wrapper

@middle
@bottom
def decorator_demo(anyString):
    print(anyString)

decorator_demo("Hello World!")