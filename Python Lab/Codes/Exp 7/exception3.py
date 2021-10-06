class User_Error(Exception):
   def __init__(self, value):
      self.value = value
   def __str__(self):
      return(repr(self.value))
try:
   raise(User_Error("User defined error"))
except User_Error as error:
   print('A New Exception occured:',error.value)