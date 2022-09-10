# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Breadth-First Search (BFS)
        if not root:
            return 0

        q = deque([(root, 1)])
        while q:
            cur, depth = q.popleft()

            if not cur.left and not cur.right:
                return depth
            if cur.left:
                q.append((cur.left, depth + 1))
            if cur.right:
                q.append((cur.right, depth + 1))

        # DFS
# def minDepth1(self, root):
#     if not root:
#         return 0
#     if None in [root.left, root.right]:
#         return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
#     else:
#         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
