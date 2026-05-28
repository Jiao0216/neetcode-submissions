"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hashmap stores old node as a key and new node as a value without any relationships
        # iterate twice 
        if not head:
            return None

        hashmap = {None:None}

        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            new_node = hashmap[cur]
            new_node.next = hashmap[cur.next]
            new_node.random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]



        