def fibo():
    first,second=0,1
    while True:
        yield first
        first,second=second,first+second

for x in fibo():
    if x>50:
        break
    print(x, end=" ")