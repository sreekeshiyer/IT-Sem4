def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
lim = int(input("Enter a limit for Fibonacci series :  "))
x = fib(lim) 
  
# Iterating over the generator object using next 
print(x.__next__()) 
print(x.__next__()) 
print(x.__next__()) 
print(x.__next__()) 
print(x.__next__()) 
  
# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop") 
for i in fib(lim):  
    print(i) 
