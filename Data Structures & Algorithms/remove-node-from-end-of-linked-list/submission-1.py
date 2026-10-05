# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # helper to reverse a list
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        # 1) reverse
        rev_head = reverse(head)

        # 2) remove nth from start in reversed list
        dummy = ListNode(0, rev_head)
        prev = dummy
        cur = rev_head
        i = 1
        while cur and i < n:
            prev = cur
            cur = cur.next
            i += 1

        # LeetCode guarantees n is valid, so cur should exist here
        prev.next = cur.next

        # 3) reverse back
        return reverse(dummy.next)