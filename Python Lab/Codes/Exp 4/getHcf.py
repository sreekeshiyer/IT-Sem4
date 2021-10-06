def computeGCD(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 
  
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print ("GCD of",a,"and",b,"=",computeGCD(a,b)) 
