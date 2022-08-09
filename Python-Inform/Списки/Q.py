l=list(map(int,input().split()))
k=int(input())
for i in range(k,len(l)-1):
    l[i]=l[i+1]
l.pop(len(l)-1)
print(*l)