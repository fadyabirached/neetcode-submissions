class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Count the total length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Step 2: Handle the edge case where we need to remove the head node
        # (e.g., list length is 5, and we want to remove the 5th from the end)
        if length == n:
            return head.next
            
        # Step 3: Find the node right before the one to be removed.
        # This node is at index (length - n - 1)
        prev = head
        for _ in range(length - n - 1):
            prev = prev.next
            
        # Step 4: Skip the target node
        prev.next = prev.next.next
        
        return head