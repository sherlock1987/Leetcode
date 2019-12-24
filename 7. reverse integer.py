class Solution(object):
    def isPalindrome(self, x):
        num = 0
        if x < 0:
            return False
        elif x%10 == 0:
            return False
        else:
            a = abs(x)
            while (a != 0):
                temp = a % 10
                num = num * 10 + temp
                a = a // 10
            if x==num:
                return True
            else:
                return False


so = Solution()
print(so.isPalindrome(123))

