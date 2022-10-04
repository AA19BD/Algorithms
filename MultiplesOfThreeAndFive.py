# def Multiples(num):
#     sum = 0
#     for i in range(1, num):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum
#
# m = Multiples(1000)
# print(m)

ans_ = [1,2,2]
set_ans = list(set(ans_))
diff = len(ans_) - len(set_ans)
# print(ans_, set_ans)
empty = ['_'] * diff
new_ans = set_ans + empty
print(new_ans)