class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        corpus_words=[]
        corpus_words = list(dict.fromkeys(nums))
        return corpus_words


nums = [1,1,2]
so = Solution()
so.removeDuplicates(nums)