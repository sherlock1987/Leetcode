class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left,right = 1,x//2
        while left<= right:
            mid = left+ (left+right)/2
            if mid * mid< x:
                left = mid+1
            else:
                right = mid-1
        return left - 1


