class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev