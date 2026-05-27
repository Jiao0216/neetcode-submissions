# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sliding window of the fast and slow pointers
        dummy = ListNode(-1)
        dummy.next = head

        slow,fast = dummy,dummy

        for _ in range(n):
            fast = fast.next # fast steps = 2
        while fast and fast.next:
             # stop at the delete node ahead which is slow.prev pointer
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
        
            
        
        

        