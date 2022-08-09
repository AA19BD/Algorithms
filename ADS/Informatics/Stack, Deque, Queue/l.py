a ,b = map(int, input().split())
for i in range(1,min(a, b)+1):
    if (max(a, b) * i) % min(a, b) == 0:
        print(max(a, b) * i)
        break

