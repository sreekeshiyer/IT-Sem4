import pickle

file = open("student.dat", "rb")
list = pickle.load(file)
print(list)
file.close()