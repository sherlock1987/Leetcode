# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def check(left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return check(left.left,right.right) and check(left.right,right.left)
        check(root.left,root.right)
TreeNode = TreeNode(object)
# aa = TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}, right: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}}

