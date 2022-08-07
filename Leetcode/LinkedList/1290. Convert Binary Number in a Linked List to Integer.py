# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_num = []
        cur = head
        while cur:
            binary_num.append(cur.val)
            cur = cur.next
        sum = 0
        for index, i in enumerate(binary_num[::-1]):
            sum += i * (2 ** index)

        return sum

