a=list(map(int, input().split()))
ans=1
for i in range(1, len(a)):
        if a[i] not in a[:i]:
            ans+=1
print(ans)