# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        nodes: List[TreeNode] = [root]

        while nodes:
            curr: TreeNode = nodes.pop(0)

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)
        
        return root

        

        