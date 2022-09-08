t = int(input())
max_num = 1000000000
for _ in range(t):
    a, b = map(int, input().split())
    print(b + ((b - 1) // (a - 1)))





