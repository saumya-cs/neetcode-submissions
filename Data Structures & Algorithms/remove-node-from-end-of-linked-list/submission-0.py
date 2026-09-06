# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        count = 0
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            if fast:
                slow = slow.next
            count += 1
        print(f"count = {count}")
        print(f"slow val = {slow.val}")
        target = count - n
        for i in range(target):
            slow = slow.next
        print(f"slow val = {slow.val}")
        if head == slow:
            head = slow.next
        else:
            slow.next = slow.next.next
        return head
        