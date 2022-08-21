# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # First Approach
        res = [low, high]

        def sum_of_nodes_in_range(root):
            if root:
                if high > root.val > low:
                    res.append(root.val)
                sum_of_nodes_in_range(root.left)
                sum_of_nodes_in_range(root.right)

        sum_of_nodes_in_range(root)
        return sum(res)

        # Second Approach
        self.sum = 0 # global sum

        def sum_of_nodes_in_range(root):
            if root:
                if high >= root.val >= low:
                    self.sum += root.val
                sum_of_nodes_in_range(root.left)
                sum_of_nodes_in_range(root.right)

        sum_of_nodes_in_range(root)
        return self.sum




