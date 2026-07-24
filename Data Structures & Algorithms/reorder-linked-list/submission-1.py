class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. count length
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        # 2. walk to the start of the second half
        steps = (n + 1) // 2
        first_tail = head
        for _ in range(steps - 1):
            first_tail = first_tail.next
        second_head = first_tail.next
        first_tail.next = None   # cut the list in two

        # 3. reverse the second half
        prev = None
        curr = second_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_head = prev  # new head of reversed second half

        # 4. merge alternately
        p1, p2 = head, second_head
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1, p2 = n1, n2