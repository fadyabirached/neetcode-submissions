# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycleChecker = set()

        while head:
            if head in cycleChecker:
                return True

            cycleChecker.add(head)
            head = head.next

        return False


