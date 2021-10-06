class FractionalQuotientError(Exception):
  pass

while(1):
  try:
    y = 100
    s = int(input("Enter a number to divide 100: "))
    assert s>=0
    z = y/s
    if (z-int(z)) != 0:
      raise FractionalQuotientError
    print("Quotient: ",z)
  except ValueError as arg:
    print("Invalid Input!",arg)
  except ArithmeticError as arg:
    print("Invalid Input!",arg)
  except FloatingPointError as arg:
    print("An error occurred while dividing!",arg)
  except AssertionError as arg:
    print("Negative Number!",arg)
  except FractionalQuotientError as arg:
    print("Quotient is fractional!")
  else: 
    print("Exit loop!")
    break
