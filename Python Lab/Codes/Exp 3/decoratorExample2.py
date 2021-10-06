def hello_decorator(func): 
    def inner1(*args, **kwargs): 
        print("before Execution") 
        returned_value = func(*args, **kwargs) 
        print("after Execution") 
        return returned_value     
    return inner1 
   
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
  
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
  
# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b))