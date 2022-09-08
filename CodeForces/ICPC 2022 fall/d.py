t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    ans = []
    ans_ = [0] * 3
    for _ in range(3):
        l = (input().split())
        ans.append(l)
        for i in l:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    count = 0
    for i in ans:
        new_ = 0
        for j in i:
            if (d[j] == 1):
                new_ += 3
            elif (d[j] == 2):
                new_ += 1
        ans_[count] = new_
        count += 1
    print(*ans_)
