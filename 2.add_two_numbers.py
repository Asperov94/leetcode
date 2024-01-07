# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return_node = iter_node = ListNode()
        num1 = ""
        num2 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        for i in (str(int(num1) + int(num2)))[::-1]:
            iter_node.next = ListNode(int(i))
            iter_node = iter_node.next
        return return_node.next
