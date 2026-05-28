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
        if not head:
            return None
        curr = head
        nodes_dict = {None: None}
        while curr:
            nodes_dict[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = nodes_dict[curr]
            copy.next = nodes_dict[curr.next]
            copy.random = nodes_dict[curr.random]
            curr = curr.next
        return nodes_dict[head]
            


        