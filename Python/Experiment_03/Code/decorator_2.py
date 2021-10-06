# demonstration of decoraters

def my_decorator(func):
    def wrapper(message):
        print("Something is happening before the function is called.")
        func(message)
        print("Something is happening after the function is called.")
    return wrapper

# syntactic sugar for decorator
@my_decorator
def say_message(message):
    print(message)

msg = input("Enter a message to print :  ")

say_message(msg)
