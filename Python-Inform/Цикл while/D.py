n=int(input())
i=0
check=0
while i<=n:
    if 2**i==n:
        check=1
    i+=1
print("YES") if check==1 else print("NO")
