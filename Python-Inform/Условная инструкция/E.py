# a=int(input())
# b=int(input())
# c=int(input())
# print(max(a,b,c))

a,b,c=int(input()),int(input()),int(input())
max=a
if b>max:
    max=b
if c>max:
    max=c
print(max)