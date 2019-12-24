class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        j = len(nums) -1
        nums.sort()
        result = []
        if nums[0]>0:
            return []
        for i in range(0,len(nums)-2,1):
            for j in range(len(nums)-1,2,-1):
                if i + j < 0:
                    tail = j -1
                    while nums[i] + nums[j] + nums[tail] != 0 and tail > i:
                        tail -=1
                    if nums[i] + nums[j] + nums[tail] == 0:
                        result.append([nums[i], nums[j], nums[tail]])
                elif i +j >= 0:
                    tail = i+1
                    while nums[i] + nums[j] + nums[tail] != 0 and tail < i:
                        tail +=1
                    if nums[i] + nums[j] + nums[tail] == 0:
                        result.append([nums[i],nums[j],nums[tail]])
                else:
                    pass
        print(result)

nums =  [-1, 0, 1, 2, -1, -4]
so = Solution()
so.threeSum(nums)

