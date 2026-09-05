"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

map original list node to corresponding new list node

for node in original nodes:

    if the node is not deep copied yet:
        create a list node with that val
        add node to map
        set random p9ointer
    
    else:
        set random pointer

setting random ptr
    if node it points to exists in map:
         point to value in map

    else:
        create node, add to map, point to value in map

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeMap = dict()
        def setRandomPointer(random_ptr):
            if not random_ptr:
                return None
            if random_ptr in nodeMap:
                return nodeMap[random_ptr]
            else:
                new_node = Node(random_ptr.val)
                nodeMap[random_ptr] = new_node
                return new_node
        if not head:
            return None
        
        new_head = Node(head.val)
        nodeMap[head] = new_head
        new_head.random = setRandomPointer(head.random)
        prev = new_head
        curr = head.next
        while curr:
            if curr not in nodeMap:
                new_node = Node(curr.val) #deep copy of node
                nodeMap[curr] = new_node #add new node to map
                prev.next = new_node #stitch list together
                new_node.random = setRandomPointer(curr.random)
                prev = new_node
                curr = curr.next
            
            else:
                existing_new_node = nodeMap[curr] #get existing new node
                prev.next = existing_new_node #stitch list together
                existing_new_node.random = setRandomPointer(curr.random)
                prev = prev.next #reset prev
                curr = curr.next
           
        return new_head
            
        