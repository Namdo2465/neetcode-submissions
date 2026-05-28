# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array1 = []
        array2 = []
        curr1 = l1
        curr2 = l2
        while curr1:
            array1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            array2.append(curr2.val)
            curr2 = curr2.next

        array1.reverse()
        array2.reverse()

        num1 = int("".join(str(num) for num in array1))
        num2 = int("".join(str(num) for num in array2))

        total = num1 + num2

        res_array = list(map(int, list(str(total)[::-1])))
        
        final_arr = []

        for num in res_array:
            final_arr.append(ListNode(num))
        for i in range(len(final_arr) - 1):
            final_arr[i].next = final_arr[i+1]
        final_arr[len(final_arr) - 1].next = None
        return final_arr[0]




