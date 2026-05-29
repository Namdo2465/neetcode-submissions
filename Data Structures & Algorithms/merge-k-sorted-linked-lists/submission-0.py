# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes_arr = []
        for k in range(len(lists)):
            head = lists[k]
            current = head
            while current:
                nodes_arr.append(current)
                current = current.next
        nodes_arr.sort(key=lambda node: node.val)
        dummy = ListNode()
        current = dummy
        for i in range(len(nodes_arr)):
            current.next = nodes_arr[i]
            current = current.next
        current.next = None
        return dummy.next

