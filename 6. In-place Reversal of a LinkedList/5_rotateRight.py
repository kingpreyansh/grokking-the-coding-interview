# coding: utf-8
# Problem: Given the head of a linked list, rotate the list to the right by k places.
# Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 4 -> 5 -> 1 -> 2 -> 3
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/rotate-list/
# Optimal solution:

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def rotateRight(head, k):
    # if the head is none return None
    if head is None:
        return head

    # get the tail of the linked list
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1

    # compute how many final rotations there are
    k = k % length
    if k == 0:
        return head

    # go to the last element in the linkedlist after k rotations
    cur = head
    for i in range(length - k - 1):
        cur = cur.next

    # fix pointers
    tmp = cur.next
    cur.next = None
    tail.next = head
    return tmp


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    rotateRight(head, 2)
