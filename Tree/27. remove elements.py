class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end  = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start +=1
        return end+1


nums = [0,1,2,2,3,0,4,2]
so = Solution()
print(so.removeElement(nums,2))
print(nums)

