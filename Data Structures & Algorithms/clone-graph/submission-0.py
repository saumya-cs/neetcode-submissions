"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneNode(self, node, old_to_new_vertices):
        
        for neighbor in node.neighbors:
            if neighbor not in old_to_new_vertices:
                newVertex = Node(neighbor.val) 
                old_to_new_vertices[neighbor] = newVertex
                self.cloneNode(neighbor, old_to_new_vertices)
            
            new_neighbor_vertex = old_to_new_vertices[neighbor]
            lst = old_to_new_vertices[node].neighbors 
            lst.append(new_neighbor_vertex)
            old_to_new_vertices[node].neighbors = lst
            
        
        
            
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #create vertices with no edges
        if node is None:
            return None
        old_to_new_vertices = dict()
        old_to_new_vertices[node] = Node(1)
        
        self.cloneNode(node, old_to_new_vertices)
        return old_to_new_vertices[node]


        