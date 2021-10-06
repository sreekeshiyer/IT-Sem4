def simpleGeneratorFun(): 
    yield "Aamir"
    yield "Z"
    yield "Ansari"
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(x.__next__())
print(x.__next__())
print(x.__next__())
