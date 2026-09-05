# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        if head is None:
            return None
        if head.next is None:
            return head
        while (head):
            stack.insert(0, ListNode(head.val))
            if (len(stack) != 1):
                stack[0].next = stack[1]
            head = head.next
        return stack[0]
        