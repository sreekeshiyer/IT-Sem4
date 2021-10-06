def numberGenerator(n):
  try:
     number = 0
     while number < n:
         yield number
         number += 1
  finally:
     yield n

print(list(numberGenerator(10)))