import numpy as np

# Defining Array 1
a = np.array([[1, 2], [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3], [2, 1]])

print("First Array:\n", a)
print("\nSecond Array:\n", b)

# Adding 1 to every element
print("\n>---------------------------< Adding >---------------------------<")
print ("\nAdding 1 to every element:\n", a + 1)

# Subtracting 2 from each element
print("\n>---------------------------< Subtracting >---------------------------<")
print ("\nSubtracting 2 from each element:\n", b - 2)

# sum of array elements
print("\n>---------------------------< Array sum >---------------------------<")
print ("\nSum of all elements of "
       "First array: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)

# transpose
print("\n>---------------------------< Transpose >---------------------------<")
print("\n Transpose of First Matrix:\n", a.transpose())

# reciprocal
arr = np.array([25, 1.33, 1, 1, 100]) 
print('\nOur array is:')
print(arr)
print('\nReciprocal of array:') 
print(np.reciprocal(arr))

# power
print("\n>---------------------------< Power >---------------------------<")
arr = np.array([5, 10, 15]) 
print('\nFirst array is:') 
print(arr)
print('\nApplying power function:') 
print(np.power(arr, 2))

# mod
print("\n>---------------------------< Mod >---------------------------<")
arr = np.array([5, 15, 20]) 
arr1 = np.array([2, 5, 9]) 
  
print('\nFirst array:') 
print(arr) 
  
print('\nSecond array:') 
print(arr1)
  
print('\nApplying mod() function:') 
print(np.mod(arr, arr1))
  
print('\nApplying remainder() function:') 
print(np.remainder(arr, arr1))
