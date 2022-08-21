# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                # print(root.val)
                inorder(root.right)

        inorder(root)
        return res

        # Iterative Approach
        res, stack = [], []
        while True:
            while root:
                stack.append(root)  # [TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}]
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

