# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1.use fast and slow pointers to cut off as half
        # 2.reverse the second group
        # 3. combine two groups
        
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        cur = head2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        l1,l2 = head,prev
        while l2:
            l1_next,l2_next = l1.next,l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
        

        



        
        

        

                
        