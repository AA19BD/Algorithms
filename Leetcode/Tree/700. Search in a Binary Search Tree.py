# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iterative Approach
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        return

        # First Recursive Approach
#         # A utility function to search a given key in BST
#         def search(root,key):

#             # Base Cases: root is null or key is present at root
#             if root is None or root.val == key:
#                 return root
#             # Key is greater than root's key
#             if root.val < key:
#                 return search(root.right,key)
#             else:
#             # Key is smaller than root's key
#                 return search(root.left,key)

#         return search(root, val)

