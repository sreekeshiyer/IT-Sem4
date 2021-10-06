import pickle

buggers = {"Aamir Ansari":1, "Isha Gawde":15, "Sreekesh Iyer":24, "Jisha Philip":27, "Kanaiya Kanabar":31, "Ninad Rao":53, "V Krishnasubramaniam":61}
filename = "debuggers"
outfile = open(filename, "wb")
pickle.dump(buggers, outfile)
outfile.close()
