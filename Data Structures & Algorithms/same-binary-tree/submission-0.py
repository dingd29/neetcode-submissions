# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        stack1.append(p)
        stack2.append(q)
        while (stack1 and stack2):
            cur1 = stack1.pop()
            cur2 = stack2.pop()
            if (not cur1 and not cur2):
                continue
            if (not cur1 or not cur2):
                return False
            if (cur1.val != cur2.val):
                return False
            stack1.append(cur1.left)
            stack1.append(cur1.right)
            stack2.append(cur2.left)
            stack2.append(cur2.right)
        return True