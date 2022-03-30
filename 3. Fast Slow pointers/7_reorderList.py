# coding: utf-8
# Problem: You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/reorder-list/
# Optimal solution:

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    if head is None or head.next is None:
        return
    # to reverse the list

    def reverseList(headOfList):
        prev, curr = None, headOfList
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # idea is to reverse the list and iterate through the original list
    # add one item in the original list
    # add one item in the reversed list
    # keep iterating through the list until one of the iterations becomes None

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # at this current stage our slow value is the middle

    headOfSecondHalf = reverseList(slow)
    headOfFirstHalf = head

    while headOfFirstHalf is not None and headOfSecondHalf is not None:
        temp = headOfFirstHalf.next
        headOfFirstHalf.next = headOfSecondHalf
        headOfFirstHalf = temp

        temp = headOfSecondHalf.next
        headOfSecondHalf.next = headOfFirstHalf
        headOfSecondHalf = temp

    if headOfFirstHalf is not None:
        headOfFirstHalf.next = None


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    print(reorderList(head))
