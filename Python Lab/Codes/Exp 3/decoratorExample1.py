#to find execution time of a function
import time 
import math 
 
def calculate_time(func): 
    def inner1(*args, **kwargs):
        begin = time.time() 
        func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 
    return inner1 

@calculate_time
def factorial(num): 
    time.sleep(2) 
    print("Factorial of",num,"=",math.factorial(num)) 

num = int(input("Enter a number:"))
factorial(num)