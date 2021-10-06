import pickle
name = input('Enter name that you want to DELETE from binary file: ')
file = open("student.dat", "rb+")
list = pickle.load(file)
found = 0
lst = []
for x in list:
    if name not in x['name']:
        lst.append(x)
    else:
        found = 1
if(found == 1):
    file.seek(0)
    pickle.dump(lst, file)
    print("Record Deleted!")
else:
    print('Name does not exist!')
file.close()