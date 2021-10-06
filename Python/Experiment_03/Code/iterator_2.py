# demonstration of iterators using __iter__ function

multiplesOfFive = [5,10,15,20,25,30]

x = iter(multiplesOfFive)
# x becomes an itertor of list "multiplesOfFive"

# we iterate through list "multiplesOfFive" using iterator "x"
print("Multiples of 5 are :")
while True:
    try:
        # next function to move to next element of the object (here, list)
        number = next(x)
        print(number)

    except StopIteration:
        break
