# Definition for singly-linked list.
#value 是这个节点的值，next 是指向下一节点的指针，
# 当 next 为空指针时，这个节点是链表的最后一个节点。
class ListNode(object):#需要自己定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode  这个注释掉的东西居然还能用。。。
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0) #dummy 的目的是要最后让指针指向起点，指向链表的首部
        print(curr)
        while l1 and l2:
            print (l1,l2)
            if l1.val <l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
l1 = [1,2,4]
l2 = [1,3,4]

so = Solution()
print(so.mergeTwoLists(ListNode(l1),ListNode(l2)))



# a=  (ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
# l1 看起来是这个样子，输入的时候 1 -2 - 4




class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while lists[0] and lists[1] and lists[2]:
            if lists[0].val <=lists[1].val and lists[0].val <=lists[2].val:
                curr.next = lists[0]
                lists[0] = lists[0].next
            elif lists[1].val <=lists[0].val and lists[1].val <=lists[2].val:
                curr.next = lists[1]
                lists[1] = lists[1].next
            else :
                curr.next = lists[2]
                lists[2] = lists[2].next
        curr = curr.next
        curr.next = lists[0] or lists[1] or lists[2]
        return dummy.next

