# coding: utf-8
# Problem: Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/reverse-linked-list-ii/
# Optimal solution: O(N)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def reverseList(head, left, right):
    dummy = Node(0, head)
    leftPrev, curr = dummy, head

    # now the curr is pointing to the left node and prev is pointing to the node before that
    # 1) reach node at position "left"
    for i in range(left - 1):
        leftPrev, curr = curr, curr.next

    # Now curr = "left", leftPrev="node before left"
    # 2) reverse from left to right
    prev = None
    for i in range(right - left + 1):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # 3) Clean up the pointers and connect the nodes
    leftPrev.next.next = curr
    leftPrev.next = prev
    return dummy.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print(reverseList(head, 2, 5))
