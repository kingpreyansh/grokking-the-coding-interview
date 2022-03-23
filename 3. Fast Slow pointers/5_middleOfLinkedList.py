# coding: utf-8
# Problem:
# Input:
# Output:
# Explanation:
# Leetcode Equivalent:
# Optimal solution:

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def middleNode(head) -> Optional[ListNode]:
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(hasCycle(head))

    head.next.next.next.next.next = head.next.next
    print(hasCycle(head))

    head.next.next.next.next.next = head.next
    print(hasCycle(head))
