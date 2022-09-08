t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a % 2 == 0 and a >= 2 * b:
        print("YES")
        print("2 " * (b - 1), a - 2 * (b - 1))
    elif a - b >= 0 and (a - b + 1) % 2 != 0:
        print("YES")
        print("1 " * (b - 1), a - b + 1)
    else:
        print("NO")



