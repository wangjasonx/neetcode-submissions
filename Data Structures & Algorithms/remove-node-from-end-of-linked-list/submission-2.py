# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        p1 = head
        dummy = ListNode(0, head)

        #dummy -> [1, 2, 3, 4, 5]

        while counter != n:
            p1 = p1.next
            counter += 1
        
        prev = dummy
        p2 = head
        while p1:
            p1 = p1.next
            prev = p2
            p2 = p2.next

        prev.next = p2.next

        return dummy.next