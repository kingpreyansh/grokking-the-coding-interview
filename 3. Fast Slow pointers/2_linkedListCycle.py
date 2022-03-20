# coding: utf-8
# Problem: Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Leetcode Equivalent: https://leetcode.com/problems/linked-list-cycle/
# Optimal solution: O(N)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def hasCycle(head):
    # we can have a fast pointer and a slow pointer
    slow, fast = head, head
    # we need to make sure the fast.next is not None then we can access fast.next.next or else we cannot
    while fast is not None and fast.next is not None:
      # fast pointer will move by 2 nodes and the slow pointer will move by 1 node
        fast = fast.next.next
        slow = slow.next
        # the second the slow pointer overlaps with the fast pointer it means that there is a cycle
        if slow == fast:
            return True
    return False


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
