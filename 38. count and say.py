class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in range(n-1):#3-2 01 duide
            seq = self.create_seq(seq)
        return seq
    def create_seq(self,seq):
        result = ''
        i = 0
        while i < len(seq):
            count = 1
            while i < (len(seq)- 1) and seq[i] ==seq[i+1]:
                i +=1
                count+=1
            result += str(count)+seq[i]
            i +=1
        return result

so = Solution()
a = so.countAndSay(4)
print(a)


