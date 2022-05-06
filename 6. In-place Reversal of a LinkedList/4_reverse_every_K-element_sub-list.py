# coding: utf-8
# Problem: Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
# Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 2 -> 1 -> 4 -> 3 -> 5
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Optimal solution: O(N)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def reverseKGroup(head, k):
    dummyNode = Node(0, head)
    groupPrev = dummyNode

    while True:
        kth = getKthNode(groupPrev, k)
        if kth is None:
            break
        groupNext = kth.next

        prev, cur = kth.next, groupPrev.next
        while cur != groupNext:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummyNode.next


def getKthNode(node, k):
    cur = node
    while cur and k > 0:
        cur = cur.next
        k -= 1
    return cur


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
