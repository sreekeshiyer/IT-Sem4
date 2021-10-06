import pickle

buggers = {"Aamir":1, "Isha":15, "Sreekesh":24, "Jisha":27, "Kanaiya":31, "Ninad":53, "Krishna":61}

filename = "debuggers"

infile = open(filename,'rb')

new_dict = pickle.load(infile)

infile.close()

print(new_dict)
print(new_dict==buggers)
print(type(new_dict))
