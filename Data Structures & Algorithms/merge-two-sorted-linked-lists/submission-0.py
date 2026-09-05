# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1 and not list2):
            return None
        if (not list1):
            return list2
        if (not list2):
            return list1
        
        tempHead1 = list1
        tempHead2 = list2
        
        if (list1.val < list2.val):
            newHead = list1
            tempHead1 = tempHead1.next
        else:
            newHead = list2
            tempHead2 = tempHead2.next
        curr = newHead
        while(tempHead1 or tempHead2):
            if (not tempHead1 and not tempHead2):
                return newHead
            if (not tempHead1):
                curr.next = tempHead2
                return newHead
            if (not tempHead2):
                curr.next = tempHead1
                return newHead
            if(tempHead1.val < tempHead2.val):
                curr.next = tempHead1
                tempHead1 = tempHead1.next
            else:
                curr.next = tempHead2
                tempHead2 = tempHead2.next
            curr = curr.next
        