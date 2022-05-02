a=int(input())
sum=0
for i in range(1,a):
    print(f'{i}*{i+1}',end="+" if i< a-1 else "=")
    sum+=i*(i+1)
print(sum)