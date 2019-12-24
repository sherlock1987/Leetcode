class  Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permuteUnique(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + j)
        cr = []
        for i in res:
            if i not in cr: cr.append(i)
        res = cr
        return res

    def permuteUnique1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:return [nums]
        res = []
        for i in range(len(nums)):#终于写对了，就加了这一行代码就可以了
            if nums[i] not in nums[:i]:
                for j in self.permuteUnique1(nums[:i]+nums[i+1:]):
                    res.append([nums[i]]+j)
        return res

print(Solution().permuteUnique([1,1,1,2]))
# class Solution:
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) <= 1:return [nums]
#         res = []
#         for i in range(len(nums)):
#             for j in self.permuteUnique(nums[:i]+nums[i+1:]):
#                 res.append([nums[i]]+j)
#         #这个写的和那个46的一模一样，写的不错，抄下来学习学习
#         #下面的代码是去重复的
#         cr = []
#         for i in res:
#             if i not in cr:
#                 cr.append(i)
#         res = cr
#         return res
#
# print(Solution().permuteUnique([1,1,2,1]))