# coding: utf-8
# Problem: Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/reverse-linked-list/
# Optimal solution: O(N)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def reverseList(head):
    prev, curr = None, head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print(reverseList(head))
