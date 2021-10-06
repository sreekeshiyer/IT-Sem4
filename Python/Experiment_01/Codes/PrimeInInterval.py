lowerLimit = int(input("Enter a lower number :  "))
upperLimit = int(input("Enter an upper number :  "))
print("Prime numbers between", lowerLimit, "and", upperLimit, "are:")
 
for num in range(lowerLimit, upperLimit + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
