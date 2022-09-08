# n = int(input())
# l1 = list(map(int, input().split()))
# m = int(input())
# l2 = list(map(int, input().split()))
#
# new_elem = []
# # for i in range(len(l1)):
# #     new_i = l1[i] # 2
# #     new_elem.append([i + new_i - 2 for i in range(1, l1[i] + 1)])
#
# sum_l1 = sum(l1)
# for i in range(1, sum_l1 + 1):
#     new_elem.append()
# print(sum_l1)

input()
L = []
r = 1
for i in input().split():
    L += [r] * int(i)
    r += 1
input()
for j in input().split():
    print(L[int(j) - 1], sep= "\n")