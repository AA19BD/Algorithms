# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #         #iteratively
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val if cur else None)

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

            if len(level) > 1:
                if level[:len(level)//2] != level[len(level)//2:][::-1]:
                    return False

        return True

        # recursively
        def helper(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and helper(n1.left, n2.right) and helper(n1.right, n2.left)

        return helper(root, root)