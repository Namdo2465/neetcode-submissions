# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False
        node_stack = []
        def findSubRoot(root, subRoot):
            nonlocal node_stack
            if not root:
                return
            if root.val == subRoot.val:
                node_stack.append(root)
            findSubRoot(root.left, subRoot)
            findSubRoot(root.right, subRoot)
        findSubRoot(root, subRoot)
        res = []
        for node in node_stack:
            res.append(isSameTree(node, subRoot))
        if True in res:
            return True
        return False