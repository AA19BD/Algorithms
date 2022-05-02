a=list(map(int,input().split()))
# list=[a[i] for i in range(len(a)) if i%2==0]
# print(list)
for i in range(len(a)):
    if i%2==0:
        print(a[i],end=" ")
    