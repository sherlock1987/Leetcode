class Solution(object):#从左边一个格子开始走，碰到阻碍了就drop，走多少算多少
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trapping = 0
        count = 0
        max_index = max(height)
        for i in range(1,max_index+1): #左边的，
            print('i',i)
            for j in range(len(height)):
                print('j',j)
                if i <= height[j]:
                    break
                else:
                    count+=1
        print('here')
        for i in range(1,max_index+1):#右边的代码
            # print('i',i)
            for j in range(len(height)-1,-1,-1):
                print('j',j)
                if i <= height[j]:
                    break
                else:
                    count+=1
        print(count)
        trapping = max_index * len(height) - count - sum(height)
        print(trapping )
        return trapping


class Solution1: #双指针法，显然要高效的多。
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, ans, min_height = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= min_height:
                ans += min_height - height[l]
                l += 1
            while l < r and height[r] <= min_height:
                ans += min_height - height[r]
                r -= 1
            min_height = min(height[l], height[r])
        print(ans)
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height1 = [3,1,2,1,3,5,3,2,1]
# so = Solution()
# so.trap(height)

so1 = Solution1   ()
so1.trap(height1)

