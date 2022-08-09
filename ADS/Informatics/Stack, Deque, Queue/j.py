def GCD(n, m):
    while n>0 and m>0:
        if n>m:
            n = n%m
        else:
            m = m%n

    return n+m

n = int(input())
m = int(input())
print(GCD(n, m))