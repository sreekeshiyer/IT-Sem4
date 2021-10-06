def avg(marks):
    try: 
        assert len(marks) != 0
        return sum(marks)/len(marks)
    except AssertionError:
        return "Empty list"

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))