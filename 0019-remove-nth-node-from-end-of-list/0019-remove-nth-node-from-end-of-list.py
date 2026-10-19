class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        i=dummy
        j=dummy
        for _ in range(n):
            j=j.next
        while j.next:
            i=i.next
            j=j.next
        i.next=i.next.next
        return dummy.next    
