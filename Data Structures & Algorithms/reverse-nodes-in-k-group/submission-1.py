# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import numpy as np

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while curr and cnt < k:
            curr = curr.next
            cnt += 1

        if cnt == k:
            curr = self.reverseKGroup(curr, k)
            while cnt > 0:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
                cnt -= 1
            head = curr
        return head


