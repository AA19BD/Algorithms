import math
n=int(input())
i=2
while i<=math.sqrt(n):
    if n%i==0:
        print(i)
        break
    i+=1
else:
    print(n)
# while n%i!=0:
#     i+=1
# print(i)

