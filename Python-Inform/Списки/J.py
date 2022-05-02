l=list(map(int,input().split()))
x= int(input())
index=0
for i in range(len(l)):
    if x>l[i]:
        print(i+1)
        break
    elif i==len(l)-1:#самый конец
        print(len(l)+1)