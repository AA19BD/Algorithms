# a,n=float(input()),int(input())

# def power(a,n):
#     if n==0: return 1
#     elif a==0:return 0
#     elif n>0:return a*power(a,n-1)
#     return 1/a*power(a,n+1)
# print(power(a,n))

a=float(input())
n=int(input())

def power(a,n):
    if n==0:
        return 1
    elif a==0:
        return 0
    elif n>0:
        return a*power(a,n-1)
    return 1/a*power(a,n+1)
print(power(a,n))

