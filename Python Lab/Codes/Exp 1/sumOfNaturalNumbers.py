num = int(input("Enter a number:"))
if num < 0:
   print("Enter a positive number")
else:
   temp = num
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum of natural nos till",temp,"is =", sum)