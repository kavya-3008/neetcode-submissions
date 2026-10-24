# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        i = 0
        if n == 1:
            prev = prev.next
        else:
            curr = prev
            i = 0

            while i < n - 2:
                curr = curr.next
                i += 1

            curr.next = curr.next.next

        curr2 = prev
        prev2 = None

        while curr2:
            nxt = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = nxt

        return prev2