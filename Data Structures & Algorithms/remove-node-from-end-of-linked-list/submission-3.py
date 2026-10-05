# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        for i in range(n):
            cur = cur.next
        if (cur is None):
            temp = head.next
            head.next = None
            return temp 
        cur = cur.next
        back = head
        while (cur is not None):
            cur = cur.next
            back = back.next
        if (back.next.next is None):
            back.next = None
            return head
        else:
            back.next = back.next.next
            return head


        