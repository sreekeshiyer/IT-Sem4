class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute
    @staticmethod
    def tostring():
        print('Student Class')
Student.tostring()