class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        i = 0
        while True:
            try:#输进去的东西是string的以及string 的各个字符
                sets = set(string[i] for string in strs)#sets 是一种数据类型，叫做集合
                print('sets is ',sets)#i 递增，然后去每一位的检验有没有相同的东西
                # print(sets.pop())#pop这个函数删除了set结构的某些东西
                # print('ok')
                if len(sets) == 1 :
                    result += sets.pop()#删除列表中的一个数值，默认是最后一个
                    print(result)
                    i+=1
                else:
                    break
            except Exception as e:
                print(e)
                break
        return result

strs = ["flower","flow","flight"]
so = Solution()
print(so.longestCommonPrefix(strs))

# #找出字符串中的重复的字符
# str='akwdlkandwm,nam,wndajbddaklwnldhawlhdlahndwla'
# dupstr=set()
# for i in str:
#     if i in str:
#         dupstr.add(i)
#
# print (dupstr)
# for i in range(0,3):
#     for j in strs[i]:
#         if j in strs[1] and j in strs[2] and j in strs[0]:
#             print(j)
#         else:
#             pass