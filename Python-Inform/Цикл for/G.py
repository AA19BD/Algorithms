n,k=int(input()),int(input())
def find(n:int)->int:
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
print(find(n)//(find(k)*find(n-k)))
