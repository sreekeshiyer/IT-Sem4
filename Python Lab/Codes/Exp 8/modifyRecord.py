import pickle
name = input('Enter name that you want to update in binary file : ')
file = open("student.dat", "rb+")
list = pickle.load(file)
found = 0
lst = []
for x in list:
    if name in x['name']:
        found = 1
        x['name'] = input('Enter new name: ')
    lst.append(x)
if(found == 1):
    file.seek(0)
    pickle.dump(lst, file)
    print("Record Updated!")
else:
    print('Name does not exist!')

file.close()