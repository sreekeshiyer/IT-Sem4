def getAscii(chr):
  return ord(chr)

char = input("Enter a character: ")
print("The ASCII value of '" + char + "' is", getAscii(char))