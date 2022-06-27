import math
n = int(input())

queue = []
res_queue = []
for i in range(n):
    a = input()
    if a.split()[0] == '+':
        queue.append(int(a.split()[1]))
    elif a.split()[0] == '-':
        res_queue.append(queue.pop(0))
    elif a.split()[0] == '*':
        p = len(queue)//2 + len(queue) % 2
        queue.insert(p, int(a.split()[1]))

for i in res_queue:
    print(i)
# print(*res_queue, sep = '\n')
# import collections
#
#
# q1 = collections.deque()
# q2 = collections.deque()
# for _ in range(int(input())):
#
#     c = input().split()
#
#     if c[0] == '+':
#         q2.append(c[1])
#     elif c[0] == '*':
#         q2.appendleft(c[1])
#     else:
#         print(q1.popleft())
#
#     if len(q1) < len(q2):
#         q1.append(q2.popleft())