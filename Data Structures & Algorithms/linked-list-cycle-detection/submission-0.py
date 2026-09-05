# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head):
            return False
        curr = head
        seen_nodes = set()
        while(curr not in seen_nodes):
            seen_nodes.add(curr)
            if(not curr.next):
                return False
            curr = curr.next
        return True
        