import math
n=int(int(input()))
def MinDivisor(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:return i
    return n
        
        
print(MinDivisor(n))