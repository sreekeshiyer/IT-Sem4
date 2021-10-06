import numpy

# Two matrices are initialized by value
x = numpy.array([[12, 6], [4, 5]])
y = numpy.array([[7, 4], [2, 9]])

#  add()is used to add matrices
print ("\nAddition of two matrices: ")
print (numpy.add(x,y))

# subtract()is used to subtract matrices
print ("\nSubtraction of two matrices : ")
print (numpy.subtract(x,y))

# divide()is used to divide matrices
print ("\nMatrix Division : ")
print (numpy.divide(x,y))

print ("\nMultiplication of two matrices: ")
print (numpy.multiply(x,y))

print ("\nThe product of two matrices : ")
print (numpy.dot(x,y))

print ("\nsquare root is : ")
print (numpy.sqrt(x))

print ("\nThe summation of elements : ")
print (numpy.sum(y))

print ("\nThe column wise summation  : ")
print (numpy.sum(y,axis=0))

print ("\nThe row wise summation: ")
print (numpy.sum(y,axis=1))

# using "T" to transpose the matrix
print ("\nMatrix transposition : ")
print (x.T)
