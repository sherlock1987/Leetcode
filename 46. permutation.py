class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <=1:
            return [nums]
        answer = []
        for i,num in enumerate(nums):
            n = nums[:i]+nums[i+1:] #成功隔离出来一个数字
            print(n)
            for y in self.permute(n):
                answer.append([num]+y)#取出来的数字，再加回去
        print('answer',answer)
        return answer

    def permute1(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        for i,num in enumerate(nums):
            n = nums[:i]+ nums[i+1:]
            for y in self.permute(n):
                answer.append([num]+y)
        return answer

nums = [1,2,3,4]
# print(nums[:0]+nums[1:])
so = Solution()
(so.permute(nums))
