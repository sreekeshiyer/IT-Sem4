try:
    age= -10
    print("Age is:")
    print(age)
    assert age>0
    yearOfBirth= 2021-age
    print("Year of Birth is:")
    print(yearOfBirth)
except AssertionError:
    print("Input Correct age.")