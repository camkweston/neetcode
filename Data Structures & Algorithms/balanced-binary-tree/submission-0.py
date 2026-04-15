# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def solve(node):
            if not node:
                return [True, 0]
            
            left = solve(node.left)
            right = solve(node.right)

            is_balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            return [is_balanced, 1 + max(left[1], right[1])]
        
        is_balanced, _ = solve(root) if root else (True, 0)
        return is_balanced


        