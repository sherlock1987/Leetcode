#变量说明, flag 的意思是针对于 IV，这种两个的数字时，i+1不能重复计算
#flag的意思是，执行完第一个if之后，第二个不必执行的意思。

class Solution(object):
    def romanToInt(self,s):
        """
        :type s: str
        :rtype: int
        MCMXCIV
        """
        RImap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        flag =2
        next =1
        for i in range(len(s)):
            print(i)
            if i<=len(s)-2 and RImap[s[i]] < RImap[s[i+1]] and flag >= 2:
               num = num + (RImap[s[i+1]]-RImap[s[i]])
               flag = 0
               next = 0

            elif i<=len(s)-1 and flag >=2 and next ==1:
               num = num + RImap[s[i]]
            next =1
            flag = flag +1
            print('num',num)
            print('flag',flag)
        return num

so = Solution()
s = 'IX'
print(so.romanToInt(s))



