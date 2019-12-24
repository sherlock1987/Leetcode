# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.num = []
        head = end = ListNode(0)
        for i in lists:
            while i:
                self.num.append(i.val)
                i = i.next
        for x in sorted(self.num):
            end.next = ListNode(x)
            end = end.next
        return head.next#这个head和这个end到底是个什么关系，为什么快要到最后冒出来个head，

