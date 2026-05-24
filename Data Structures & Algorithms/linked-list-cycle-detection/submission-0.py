# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()
        if not head:
            return False
        current = head
        while current:
            if current in visited_node:
                return True
            visited_node.add(current)
            current = current.next
        return False
        