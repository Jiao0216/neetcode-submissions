# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # use carry to handle over 10
        # dummy node to start 

        dummy = ListNode(-1)
        cur = dummy

        carry =0
        
        # if the val ==0 add 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

        # deal with the sum
        # if no l1 and l2 then add carry
        
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10
            cur.next = ListNode(val)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next



        



        