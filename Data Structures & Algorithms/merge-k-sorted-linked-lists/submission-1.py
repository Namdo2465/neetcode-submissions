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
            while head:
                nodes_arr.append(head.val)
                head = head.next
        nodes_arr.sort()
        prev = ListNode(0)
        if len(nodes_arr) == 0:
            return None
        prev.next = ListNode(nodes_arr[0])
        current = prev.next
        for i in range(1, len(nodes_arr)):
            current.next = ListNode(nodes_arr[i])
            current = current.next
        current.next = None
        return prev.next

