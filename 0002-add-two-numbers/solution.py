# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        total = self.strSum(l1) + self.strSum(l2)

        temp = ListNode(0)
        curr = temp
        for x in reversed(str(total)):
            curr.next = ListNode(int(x)) 
            curr = curr.next
        return temp.next


    
    def strSum(self, head):
        curr = head
        num = ""
        while curr:
            num += str(curr.val)
            curr = curr.next
        return int(num[::-1])

