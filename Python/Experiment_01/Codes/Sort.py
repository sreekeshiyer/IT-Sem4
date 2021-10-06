list = []
n = int(input("Enter number of elements in the list:"))
print("Enter",n,"elements into the list:")
for i in range(n):
    a = int(input())
    list.append(a)
print("Entered list:",list)
for iter_num in range(len(list)-1,0,-1):
    for idx in range(iter_num):
        if list[idx]>list[idx+1]:
             temp = list[idx]
             list[idx] = list[idx+1]
             list[idx+1] = temp
print("Sorted list:",list)
