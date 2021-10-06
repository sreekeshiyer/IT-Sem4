num = int(input("Enter a number:"))
my_list = range(150)
result = list(filter(lambda x: (x % num == 0), my_list))
print("Numbers divisible by",num,"are",result)