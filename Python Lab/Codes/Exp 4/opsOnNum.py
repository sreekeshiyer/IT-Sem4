def factorial(n):
  if n == 1:
    return n
  else:
    return n*factorial(n-1)

def reverse(n, r):
  if n==0:
    return r
  else:
    return reverse(n//10, r*10 + n%10)

def testArmstrong(n):
  order = len(str(n))
  sum = 0
  temp = n
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
  return(sum)

def testPalindrome(n):
  rev = 0
  while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
  return(rev)

def testPrime(n):
  flag = 0
  if n > 1:
    for i in range(2, n):
      if (n % i) == 0:
        flag = 1
        break
  return(flag)

def fibonacciSeries(n):
  if n <= 1:
    return n
  else:
    return(fibonacciSeries(n-1) + fibonacciSeries(n-2))

while True:
  print("\nSelect operation:")
  print("1. Factorial")
  print("2. Reverse")
  print("3. Test Armstrong number")
  print("4. Test Palindrome number")
  print("5. Test Prime number")
  print("6. Fibonacci Series")
  choice = input("Enter choice(1/2/3/4/5/6): ")
  if choice in ('1', '2', '3', '4', '5', '6'):
    
    if choice == '1':
      num = int(input("Enter a number: "))
      print("The factorial of", num, "is", factorial(num))
    
    elif choice == '2':
      num = int(input("Enter a number: "))
      reversed_number = reverse(num,0)
      print("Reverse of %d is %d" %(num, reversed_number))
    
    elif choice == '3':
      num = int(input("Enter a number: "))
      new_num = testArmstrong(num)
      if num == new_num:
        print(num,"is an Armstrong number")
      else:
        print(num,"is not an Armstrong number")
    
    elif choice == '4':
      num = int(input("Enter a number: "))
      new_num = testPalindrome(num)
      if num == new_num:
        print(num,"is a Palindrome number")
      else:
        print(num,"is not a Palindrome number")
    
    elif choice == '5':
      num = int(input("Enter a number: "))
      flag = testPrime(num)
      if flag == 0:
        print(num,"is a Prime number")
      else:
        print(num,"is not a Prime number")

    elif choice == '6':
      num = int(input("Enter a number: "))
      if num <= 0:
        print("Please enter a positive integer")
      else:
        print("Fibonacci sequence:")
      for i in range(num):
        print(fibonacciSeries(i),end=" ")
    
    else:
      break
      quit()