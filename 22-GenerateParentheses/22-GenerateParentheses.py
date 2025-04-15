# Last updated: 4/14/2025, 9:41:26 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
          return head

        p = head
        while p is not None:
          q = p.next 
          if q is None:
            break
          t = p.val
          p.val = q.val
          q.val = t
          p = q.next

        return head
        