# demonstration of decorators

def betterDivide(func):
    def innerFunction(a, b):
        print(f"Dividing {a} by {b}")
        if (b == 0):
            print("Can not be divided!")
            return
        return func(a, b)
    return innerFunction

# decorate divide function
def divide(a ,b):
    print(a/b)
divide = betterDivide(divide)

# calling function
a = int(input("Enter a number :  "))
b = int(input("Enter another number :  "))
divide(a,b)
