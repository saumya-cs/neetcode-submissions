# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#first -> last -> second -> second last
# a b c d e f g.  how many forward? 6 4 2 0
# a g b f c e d

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        left = head
        right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        #reverse right half
        curr = left.next
        left.next = None
        
        prev = None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        head2 = prev
        first = head
        second = head2
        while second:
            tmp1 = first.next
            tmp2 = second.next
            #a -> b -> c    1 -> 2 -> 3
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        return