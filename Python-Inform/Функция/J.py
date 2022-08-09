import math
from tabnanny import check
n=int(int(input()))

def isPrime(n):
    check=True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return check==0
    return check
        
        
print("YES") if isPrime(n) else print("NO")

