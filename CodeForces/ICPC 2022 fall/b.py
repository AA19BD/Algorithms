t = int(input())
for _ in range(t):
    n = int(input())
    count = 1
    ans = []
    while n:
        if n % 10 != 0:
           ans.append( int(n % 10 * count))
        n //= 10
        count *= 10
    print(len(ans))
    print(*ans)