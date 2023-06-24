class Node:
    def __init__(self, val=0, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt


class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.size = 0
        self.head.nxt, self.tail.pre = self.tail, self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index < (self.size + 1) >> 1:
            cur = self.head.nxt
            for _ in range(index):
                cur = cur.nxt
        else:
            cur = self.tail.pre
            for _ in range(self.size - index - 1):
                cur = cur.pre
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        self.head.nxt.pre, self.head.nxt, node.nxt, node.pre = node, node, self.head.nxt, self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        self.tail.pre.nxt, self.tail.pre, node.pre, node.nxt = node, node, self.tail.pre, self.tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.size:
            if index < (self.size + 1) >> 1:
                node = Node(val)
                cur = self.head
                for _ in range(index):
                    cur = cur.nxt
                cur.nxt.pre, cur.nxt, node.nxt, node.pre = node, node, cur.nxt, cur
            else:
                node = Node(val)
                cur = self.tail
                for _ in range(self.size - index):
                    cur = cur.pre
                cur.pre.nxt, cur.pre, node.pre, node.nxt = node, node, cur.pre, cur
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            if index < (self.size + 1) >> 1:
                cur = self.head
                for _ in range(index):
                    cur = cur.nxt
                cur.nxt.nxt.pre, cur.nxt = cur, cur.nxt.nxt
            else:
                cur = self.tail
                for _ in range(self.size - index - 1):
                    cur = cur.pre
                cur.pre.pre.nxt, cur.pre = cur, cur.pre.pre
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)