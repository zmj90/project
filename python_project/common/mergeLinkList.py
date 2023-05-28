"""
【3】输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def merge(self, head1, head2):
        # 加一个无用的节点便于比较
        h1 = Node(None)
        h1.next, head1 = head1, h1

        while h1.next:
            if h1.next.value < head2.value:
                h1 = h1.next
                continue
            tmp, h1.next = h1.next, head2
            head2, h1 = tmp, h1.next
        h1.next, head1 = head2, head1.next
        return head1


if __name__ == '__main__':
    s = Solution()
    head1 = Node(100)
    head1.next = Node(200)
    head1.next.next = Node(300)
    head1.next.next.next = Node(900)
    head2 = Node(80)
    head2.next = Node(400)
    head2.next.next = Node(1000)

    re = s.merge(head1, head2)
    del head1, head2
    while re:
        print(re.value, end=' ')
        re = re.next
    print()

