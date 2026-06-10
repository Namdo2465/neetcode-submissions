# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes_arr = []
        def dfs(node):
            nonlocal nodes_arr
            if not node:
                return
            if node:
                nodes_arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        nodes_arr.sort()
        return nodes_arr[k-1]
