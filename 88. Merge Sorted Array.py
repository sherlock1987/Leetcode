class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        buf = [0 for x in range(len(nums1))]

        while i < m and j <n:
            if nums1[i] <= nums2[j]:
                buf[k] = nums1[i]
                i+=1
            elif nums1[i] > nums2[j]:
                buf[k] = nums2[j]
                j+=1
            k+=1
        print(buf)
        print(k)
        for l in range(m-i+n-j):# 3-3+3-1 = 2
            print('L',l)
            print('k+l',k+l)
            if i < m:
                i+=1
                buf[k+l] = nums1[i]
            elif j < n:
                print('J',j)
                buf[k+l] = nums2[j]
                j+=1
        print(buf)


    def merge2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n] #完全看不懂，我的脑子已经迷糊了，debug去,差不多读懂了，但还是不是很理解，把
            #56放了之后的骚操作


so =Solution()
so.merge2([1,2,3,0,0,0],3,[2,5,6],3)

#总结这道题主要考察了我的思维能力了，不是很难，但是花了我一个小时左右去解决它。
#结果不正确，草，即便是赋值给nums1也不行，为什么呢