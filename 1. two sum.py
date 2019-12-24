class Solution:
    def twoSum(self,num,target):
        dict = {}
        for i in range(len(num)):
            print(i)
            if (target-num[i]) not in dict:
                dict[num[i]] = i
            elif (target-num[i]) in dict:
                print ('zoujinlaile')
                return [dict[target - num[i]],i]
        print(dict)


target = 9
num = [2,11,9,11]
so = Solution()
a = so.twoSum(num,target)
# print(so.twoSum(num,target))
print (a)

