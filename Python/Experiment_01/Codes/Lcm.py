x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
 
if x > y:
    greater = x
else:
    greater = y
 
while(True):
    if((greater % x == 0) and (greater % y == 0)):
        lcm = greater
        break
    greater += 1
 
print("The L.C.M. is",lcm)
