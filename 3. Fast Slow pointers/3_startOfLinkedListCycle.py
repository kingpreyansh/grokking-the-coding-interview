# coding: utf-8
# Problem: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Leetcode Equivalent: https://leetcode.com/problems/linked-list-cycle-ii/
# Optimal solution: O(N)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def detectCycle(head):
    # phase 1 - find the intersection point
    def findIntersection(head):
        p1, p2 = head, head
        while p2 is not None and p2.next is not None:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                return p1  # this is the intersection point
        return None

    if head is None:
        return None
    intersectionP = findIntersection(head)
    if intersectionP is None:
        return None

    # now we have the intersection and phase 2 begins
    # one pointer is at the head and one pointer is at the intersection
    # iterate through the nodes - node by node and when the nodes meet it will be the head
    # if the cycle exists ofc ^
    p1 = head
    p2 = intersectionP

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1.val


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(0)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    print(detectCycle(head))

    head.next.next.next = head.next
    print(detectCycle(head))
