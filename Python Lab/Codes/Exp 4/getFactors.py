num = int(input("Enter a number: "))
my_list = []

for i in range(1, num + 1):
    my_list.append(i)

new_list = list(filter(lambda x: (num % x == 0), my_list))
print("Factors of",num,":",new_list)