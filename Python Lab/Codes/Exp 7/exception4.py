class NegativeAgeError(Exception):
    pass
try:
    age= -10
    print("Age is:")
    print(age)
    if age<0:
        raise NegativeAgeError
    yearOfBirth= 2021-age
    print("Year of Birth is:")
    print(yearOfBirth)
except NegativeAgeError:
    print("Input Correct age.")