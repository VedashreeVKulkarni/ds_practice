# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        if left==right:
            return head
        else:
            prev=dummy
            for _ in range(left-1):
                prev=prev.next
            rev_prev=None 
            cur=prev.next
            temp1=cur
            temp2=prev   
            for _ in range(right-left+1):
                next=cur.next
                cur.next=rev_prev
                rev_prev=cur
                cur=next
            temp1.next=cur
            temp2.next=rev_prev  
            return dummy.next
        