# Definition for a binary tree node.
#easy 关键是调用isSameTree那边，别忘记了。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if q.val == p.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
        else:
            return False