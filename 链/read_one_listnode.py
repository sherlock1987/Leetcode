class ListNode(object):
    def _init_(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def print_listnode(self):
        list = []
        while(ListNode):
            list.append(ListNode.val)
            ListNode = ListNode.next


