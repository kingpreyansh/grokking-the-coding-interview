# coding: utf-8
# Problem: Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
# Input: [12, 7, 1, 9, None, 10, 5], node = 9
# Output: 10
# Explanation:
# Leetcode Equivalent:
# Optimal solution:

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderSuccessor(root, key):
    q = deque()
    if root is None:
        return -1
    q.append(root)
    ret = []
    while q:
        qLen = len(q)
        for i in range(qLen):
            node = q.popleft()
            if node:
                if node.val is not None:
                    ret.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    for i in range(len(ret)):
        if ret[i] == key:
            if i + 1 < len(ret):
                return ret[i + 1]

    return -1


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(None)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(levelOrderSuccessor(root, 9))
