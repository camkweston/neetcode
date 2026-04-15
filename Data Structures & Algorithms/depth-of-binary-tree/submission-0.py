# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], curr_depth: int = 0) -> int:

        if not root:
            return curr_depth
        else:
            return max(
                self.maxDepth(root.left, curr_depth + 1),
                self.maxDepth(root.right, curr_depth + 1)
            )
        




        