# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        cnt = 1
        while curr.next:
            cnt += 1
            curr = curr.next
        curr2 = head
        cnt2 = 1
        if cnt - n == 0:
            if cnt == 1:
                return None
            head = curr2.next
        while cnt2 < cnt - n:
            curr2 = curr2.next
            cnt2 += 1
        curr2.next = curr2.next.next
        return head
        
        