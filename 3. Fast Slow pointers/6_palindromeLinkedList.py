# coding: utf-8
# Problem: Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true
# Explanation: The linked list is a palindrome
# Leetcode Equivalent: https://leetcode.com/problems/palindrome-linked-list/
# Optimal solution: O(N)

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def isPalindrome(head):
    p1, p2 = head, head
    # edge cases where if there is 0 or 1 node it is automatically a palindrome
    if head is None or head.next is None:
        return True

     # to do it in O(1) space time we need to keep the same array
    def reverse(headOfMiddle):
        prev, curr = None, headOfMiddle
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  # new head

    # get the midpoint to reverse
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next

    midPoint = reverse(p1)
    copyMidPoint = midPoint

    while head is not None and midPoint is not None:
        if head.val != midPoint.val:
            break
        head = head.next
        midPoint = midPoint.next

    reverse(copyMidPoint)

    if head is None or midPoint is None:
        return True

    return False


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    print(isPalindrome(head))
