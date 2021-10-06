import numpy as np
import random

# Creating 1D Array
arr_1D = np.array([1, 2, 3])
print("Array One dimension :  \n",arr_1D)
 
# Creating 2D Array
arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray with Two dimension :  \n", arr_2D)

# Creating nD array
n = int(input("\nEnter the dimension of array to create :  "))
nDarray = np.zeros([n, random.randint(1,4)])
print("\nExample of empty array of dimension",n,"is : \n",nDarray)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)


