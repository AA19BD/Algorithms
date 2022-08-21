# Definition for a binary Tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        if root and root.left is None and root.right is None:
            return [root.val]

        ans = []

        def postorder_traversal(root):
            if root:
                postorder_traversal(root.left)
                postorder_traversal(root.right)
                ans.append(root.val)

        postorder_traversal(root)
        return ans


