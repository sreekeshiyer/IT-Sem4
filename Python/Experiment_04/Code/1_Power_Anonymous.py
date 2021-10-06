numerOfTerms = 10
result = list(map(lambda x: 2 ** x, range(numerOfTerms)))
print("Number of terms are:",numerOfTerms)
for i in range(numerOfTerms):
    print("2 raised to power",i,"is",result[i])
