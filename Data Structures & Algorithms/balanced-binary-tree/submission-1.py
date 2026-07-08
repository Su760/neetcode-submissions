# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(curr):
            if not curr:
                return 0

            return 1 + max(dfs(curr.left), dfs(curr.right))
        
        left = dfs(root.left)
        right = dfs(root.right)

        if abs(right - left) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False