l=list(map(int,input().split()))
max=None
index=0
for i in range(len(l)):
    # if max is None:
    #     max=l[i]
    if  l[i]>l[index]:
        # max=l[i]
        index=i
print(l[index],index)