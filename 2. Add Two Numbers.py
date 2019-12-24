# Definition for singly-linked list.
#注意的有亮点
#dummy。next
#
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(0)
        result = dummy

        while l1 and l2:
            result.next = ListNode((flag + l1.val + l2.val) % 10)
            flag = (flag + l1.val + l2.val) // 10
            l1 = l1.next
            l2 = l2.next
            result = result.next

        if l1:
            while l1:
                result.next = ListNode((flag + l1.val) % 10)
                flag = (flag + l1.val) / 10

        if l2:
            while l2:
                result.next = ListNode((flag + l2.val) % 10)
                flag = (flag + l2.val) / 10
        if flag == 1:
            result.next = ListNode(flag)

        return dummy.next
