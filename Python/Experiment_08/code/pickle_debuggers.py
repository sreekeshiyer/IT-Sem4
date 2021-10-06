import pickle

buggers = {"Aamir":1, "Isha":15, "Sreekesh":24, "Jisha":27, "Kanaiya":31, "Ninad":53, "Krishna":61}

filename = "debuggers"

outfile = open(filename, "wb")

pickle.dump(buggers, outfile)

outfile.close()
