# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head  # First Approach
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:  # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

        # cur = head # Second Approach
        # stack_ = []
        # while cur:
        #     stack_.append(cur.val)
        #     cur = cur.next
        # # print(stack_)
        # for i in range(0, len(stack_)):
        #     print(stack_[len(stack_) - i - 1])
        #     if not (stack_[i] == stack_[len(stack_) - i - 1]):
        #         return False
        # return True