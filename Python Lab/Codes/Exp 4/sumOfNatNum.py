def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)
num = int(input("Enter a number: "))
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is",recur_sum(num))