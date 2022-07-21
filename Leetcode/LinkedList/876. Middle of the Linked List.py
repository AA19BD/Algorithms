# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #         cur = head
        #         list_ = [head.val]
        #         if head:
        #             while cur.next:
        #                 cur = cur.next
        #                 list_.append(cur.val)

        #         for i in range(len(list_)//2):
        #             head = head.next
        #         return head

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow