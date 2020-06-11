# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dList = ListNode()
        dPtr = dList
        
        while l1 and l2:
            if(l1.val < l2. val):
                dList.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dList.next = ListNode(l2.val)
                l2 = l2.next
            dList = dList.next
        if l1:
            dList.next = l1
        else:
            dList.next = l2
        
        return dPtr.next