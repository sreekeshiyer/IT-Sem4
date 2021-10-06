import pickle
buggers = {"Aamir Ansari":1, "Isha Gawde":15, "Sreekesh Iyer":24, "Jisha Philip":27, "Kanaiya Kanabar":31, "Ninad Rao":53, "V Krishnasubramaniam":61}
filename = "debuggers"
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(new_dict==buggers)
print(type(new_dict))
