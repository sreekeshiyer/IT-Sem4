# AssertionError
def assertionError(n1, n2):
    try:
        assert n2 != 0, "Invalid Operation"
        print(n1 / n2)

    # the errror_message provided by the user gets printed 
    except AssertionError as msg: 
        print(msg)

# ImportError
def importError():
    try:
        from mypackage import greet
    except Exception as e:
        print(e)

# IndexError
def indexError(index):
    try:
        arr = [5, 10, 15, 20, 25]
        print("Size of array is 5")
        print(arr[index])
    except IndexError as e:
        print(e)

# KeyError
def keyError(key):
    try:
        dict = {"one": "Lorem", "two": "Ipsum", "three": "Dolor", "four": "Sit"}
        print("Dictionary have 4 keys (from one to four)")
        print(dict[key])
    except KeyError as e:
        print("Key not found",e)

# NameError
def nameError():
    try:
        knownVariable = 20
        print(knownVariable)
        print(unknownVariable)
    except NameError as e:
        print(e)

# OverflowError
def overflowError():
    i=1
    try:
        f = 3.0**i
        for i in range(100):
            print(i, f)
            f = f ** 2
    except OverflowError as err:
        print('Overflowed after ', f, err)

# SyntaxError
def syntaxError():
    try:
        print('Valid syntax')
        print(eval('**Not Valid Syntax**'))

    except SyntaxError as err:
        print (err)

# ValueError
def valueError():
    try:
        print (float('Aamir'))
    except ValueError as e:
        print (e)

# ZeroDivisionError
def zeroDivisionError(n):
    try:
        print(20/n)

    except ZeroDivisionError as msg: 
        print(msg)

choice = 0
while (True):
    print("""
    1. AssertionError       6. OverflowError
    2. ImportError          7. SyntaxError
    3. IndexError           8. ValueError
    4. KeyError             9. ZeroDivisionError
    5. NameError            10. EXIT
    """)
    choice = int(input("Enter your choice :  "))

    if (choice == 1):
        print("Enter two numbers to divide")
        n1 = int(input("Enter number 1 :  "))
        n2 = int(input("Enter number 2 :  "))
        assertionError(n1, n2)

    elif (choice == 2):
        importError()

    elif (choice == 3):
        index = int(input("Enter an index (between 0 to 4) :  "))
        indexError(index)
    
    elif (choice == 4):
        key = input("Enter a key (between `one` to `four`) :  ")
        keyError(key)

    elif (choice == 5):
        nameError()

    elif (choice == 6):
        overflowError()

    elif (choice == 7):
        syntaxError()

    elif (choice == 8):
        valueError()
    
    elif (choice == 9):
        n = int(input("Enter a number to divide from :  "))
        zeroDivisionError(n)
    
    elif (choice == 10):
        print("*** E X I T I N G ***")
        break;
    else:
        print("Invalid choice")

