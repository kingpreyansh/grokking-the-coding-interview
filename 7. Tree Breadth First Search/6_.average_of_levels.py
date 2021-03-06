# coding: utf-8
# Problem: Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Leetcode Equivalent: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Optimal solution:

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root):
    q = deque()
    if root is None:
        return []
    q.append(root)
    q.append(None)
    ret = []
    while q:
        level, qLen = [], len(q)
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        if level:
            avg = sum(level)/len(level)
            ret.append(avg)

    return ret


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    levelOrderBottom(root)
