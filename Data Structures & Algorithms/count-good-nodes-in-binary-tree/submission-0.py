# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, sofarMax):
            if not node:
                return
            nonlocal count
            if node.val >= sofarMax:
                count += 1
                sofarMax = node.val
            dfs(node.left, sofarMax)
            dfs(node.right, sofarMax)
        dfs(root, root.val)
        return count
