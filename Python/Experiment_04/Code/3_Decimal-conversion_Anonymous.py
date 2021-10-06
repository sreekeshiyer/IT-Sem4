num1 = int(input("Enter a decimal number: "))
bin=lambda x : format(x,'b')
print("Equivalent binary number is",bin(num1))

num2 = int(input("Enter a decimal number: "))
bin=lambda x : format(x,'o')
print("Equivalent octal number is",oct(num2))

num3 = int(input("Enter a decimal number: "))
bin=lambda x : format(x,'x')
print("Equivalent hexadecimal number is",hex(num3))
