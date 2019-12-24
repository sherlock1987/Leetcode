class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n ==0:
            return False
        Solution.helper(self,n,n,n,result,'')
        print(result)
        return result

    def helper(self,l,r,n,result,item):
        """
        :type l,r,n: int
        :rtype: List[str]
        """
        if r < l:
            return
        if l==0 and r ==0:
            result.append(item)
        if l > 0:
            Solution.helper(self, l-1, r, n, result, item+ '(')
        if r > 0:
            Solution.helper(self, l, r-1, n, result, item+ ')')

so = Solution()
so.generateParenthesis(3)


