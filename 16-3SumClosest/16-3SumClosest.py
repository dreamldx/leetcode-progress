# Last updated: 4/2/2025, 8:46:05 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
            
        ahead = head
        for i in range(1, n+1):
            ahead = ahead.next
            if ahead == None:
                return head.next
        
        p = head
        while(True):
            ahead = ahead.next
            print(p.val)
            if ahead == None:
                p.next = p.next.next
                break
            p = p.next

           

        return head