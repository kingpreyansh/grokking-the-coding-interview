# coding: utf-8
# Problem: Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Optimal solution:

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root):
    q = deque()
    if root:
        q.append(root)
    result = []
    while q:
        levels = []
        qLength = len(q)
        for i in range(qLength):
            node = q.popleft()
            if node:
                levels.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if levels:
            result.append(levels)

    result.reverse()
    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
