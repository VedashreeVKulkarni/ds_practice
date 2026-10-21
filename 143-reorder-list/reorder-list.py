class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        first=head
        slow=head
        fast=head
        second=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        cur=second
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        second=prev
        while second:    
            temp1 = first.next
            temp2 = second.next
            first.next=second 
            second.next=temp1
            first=temp1
            second=temp2


        
   
        