t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    if a.replace('G', 'B') == b.replace('G', 'B'):
        print('YES')
    else:
        print('NO')