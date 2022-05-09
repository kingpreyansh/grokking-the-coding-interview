# coding: utf-8
# Problem: Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
# Input: [1, 2, 3, 4, 5, 6, 7]
# Output: [[1], [2, 3], [4, 5, 6, 7]]
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Optimal solution:

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    # create a queue
    q = deque()
    result = []
    # add the first element to the queue if its not null
    if root:
        q.append(root)

    # keep iterating through the queue while it's non-empty
    while q:
        # array to keep track of nodes in each level
        level, qLen = [], len(q)
        for i in range(qLen):
            # if node is not empty add its children to the queue
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        # at this point the level should be done
        if level:
            result.append(level)

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    levelOrder(root)
