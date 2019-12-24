class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        if s =='':
            return result
        ls = s.split()
        print(ls)
        if ls == []:
            print('yes')
            return result
        for i in reversed(range(1, len(ls))):
            print(i)
            result += ls[i]+' '
        result += ls[0]
        print(result)

s = "the sky is blue"
s = " "
so = Solution()
so.reverseWords(s)