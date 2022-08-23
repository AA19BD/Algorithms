# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []

        def preorder(root):
            if root:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return ans