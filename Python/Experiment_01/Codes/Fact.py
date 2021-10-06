
num = int(input("Enter a number :  "))
factorial = 1
 
if num < 0:
   print("Factorial does not exist")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(factorial)
