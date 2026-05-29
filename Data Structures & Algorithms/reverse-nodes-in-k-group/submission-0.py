# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import numpy as np

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        cnt = 0
        while curr:
            cnt += 1
            curr = curr.next
        grp = cnt // k
        nodes = [[None] * k for _ in range(grp + 1)]
        curr = head
        cnt = 0
        idx = 0
        while curr:
            if idx == grp:
                nodes[idx][cnt] = curr
                cnt += 1
            else:
                nodes[idx][k - cnt - 1] = curr
                cnt += 1
                if cnt > k-1:
                    idx += 1
                    cnt = 0
            curr = curr.next
        final = []
        for i in range(len(nodes)):
            for j in range(k):
                if nodes[i][j] is not None:
                    final.append(nodes[i][j])
        res = ListNode()
        dummy = res
        for node in final:
            dummy.next = node
            dummy = dummy.next
        dummy.next = None
        return res.next
            


