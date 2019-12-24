import collections
from pybst.bstree import BSTree
from pybst.draw import plot_tree


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def getsubtree(nums,start,end):
            if start==end:
                return None
            max_=max(nums[start:end])
            node=TreeNode(max_)
            node.left=getsubtree(nums,start,nums.index(max_))
            node.right=getsubtree(nums, nums.index(max_)+1, end)
            return node

        return getsubtree(nums, 0, len(nums))
solutions = Solution()