
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        cur = self.left.next
        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        if cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prev = self.left
        nxt = self.left.next

        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        cur = self.left.next
        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        if index != 0:
            return

        node = ListNode(val)
        prev = cur.prev

        node.prev = prev
        node.next = cur
        prev.next = node
        cur.prev = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        cur = self.left.next
        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        if cur == self.right or index != 0:
            return

        prev = cur.prev
        nxt = cur.next
        prev.next = nxt
        nxt.prev = prev
