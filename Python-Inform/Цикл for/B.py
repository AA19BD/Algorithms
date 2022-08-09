a,b=int(input()),int(input())
def increase(a,b):
    for i in range(a,b+1):
        print(i)
def decrease(a,b):
    for i in range(a,b-1,-1):
        print(i)
if a<b:
    increase(a,b)
else:
    decrease(a,b)

