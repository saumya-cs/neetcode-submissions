# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        dummyHead = ListNode()
        curr = dummyHead
        while one or two:
            if not one:
                curr.next = two
                return dummyHead.next
            if not two:
                curr.next = one
                return dummyHead.next
            if one.val <= two.val:
                curr.next = one
                one = one.next
            else:
                curr.next = two
                two = two.next
            curr = curr.next
        return dummyHead.next


        