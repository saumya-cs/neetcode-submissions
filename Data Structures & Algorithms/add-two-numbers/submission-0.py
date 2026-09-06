# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = l1
        two = l2
        carry = 0
        level = 0
        total = 0
        dummy = ListNode()
        curr = dummy
        while one or two:
            if one:
                val1 = one.val
            else:
                val1 = 0
            
            if two:
                val2 = two.val 
            else:
                val2 = 0

            local_sum = val1 + val2
            print(local_sum)
            if local_sum > 9:
                carry = int(str(abs(local_sum))[0])
            else:
                carry = 0
            new_sum = local_sum % 10
            curr.next = ListNode(new_sum)
            curr = curr.next
            level += 1
            one = one.next
            two = two.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
        