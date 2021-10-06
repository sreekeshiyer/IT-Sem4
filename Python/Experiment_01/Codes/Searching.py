
list = []
n = int(input("Enter number of elements in the list:"))
print("Enter",n,"elements into the list:")
for i in range(n):
    a = int(input())
    list.append(a)
print("Entered list:",list)
search_for = int(input("Enter number to be searched:"))
search_at = 0
search_res = False	
while search_at < len(list) and search_res is False:
    if list[search_at] == search_for:
        search_res = True
    else:
        search_at = search_at + 1
if search_res:
    print(search_for,"is FOUND in the list")
else:
    print(search_for,"is NOT FOUND in the list")

