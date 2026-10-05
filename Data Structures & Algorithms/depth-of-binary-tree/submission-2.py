# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        stack.append([root, 1])
        maxi = 1
        while stack:
            node, count = stack.pop()
            if node.right:
                stack.append([node.right,count+1])
                maxi = max(maxi, count+1)
            if node.left:
                stack.append([node.left,count+1])
                maxi = max(maxi, count+1)
        return maxi