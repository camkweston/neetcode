# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getPathFromRootToNode(self, curr: TreeNode, target: TreeNode, res: list):
        res.append(curr)
        if curr.val == target.val:
            return res
        elif curr.val > target.val:
            return self.getPathFromRootToNode(curr.left, target, res)
        else:
            return self.getPathFromRootToNode(curr.right, target, res)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_from_root_to_p = self.getPathFromRootToNode(root, p, [])
        path_from_root_to_q = self.getPathFromRootToNode(root, q, [])

        lca = root

        for a,b in zip(path_from_root_to_p, path_from_root_to_q):
            if a == b:
                lca = a
            else:
                break
        
        return lca



        