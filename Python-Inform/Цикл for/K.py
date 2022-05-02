a,b=int(input()),int(input())
for i in range(a,b-(b%2)+1,2):
    print(i%2+i,end=" ")