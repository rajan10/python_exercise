def decorator_star(func):
    def inner():
        print("****")
        func()
        print("****")

    return inner  # returning inner function


def decorator_hash(func):
    def inner():
        print("####")
        func()
        print("####")

    return inner  # returning inner function

@decorator_star
@decorator_hash
def normal():
    print("I am a normal function")

# normal()

# hashed_inner = decorator_hash(normal)
# stared_inner = decorator_star(hashed_inner)
# stared_inner()