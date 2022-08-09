l=list(map(int,input().split()))
min_index=10e10
for i in range(len(l)):
    if l[i]>0 and l[i]<min_index:
        min_index=l[i]
print(min_index)