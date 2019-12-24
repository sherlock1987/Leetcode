class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        local_count = 0
        for i in ((s)):
            if i == ' ':
                local_count=0
            else:
                local_count+=1
                count=local_count
        return count