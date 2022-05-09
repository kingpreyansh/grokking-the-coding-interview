# coding: utf-8
# Problem: Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Explanation:
# Leetcode Equivalent: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Optimal solution:

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMinDepth(root):
    # do BFS i.e go level by level until a leaf node is found - the depth of that node will be the minimum depth of the entire tree
    q = deque()
    # if there is no nodes then return 0
    if root is None:
        return 0
    # to start the queue off
    q.append(root)
    minDepth = 0
    # while the queue is not empty
    while q:
        # keep going level by level increasing the minDepth variable
        minDepth += 1
        levelLength = len(q)
        # iterate every node for the level
        for i in range(levelLength):
            node = q.popleft()
            # leaf node
            if node:
                if node.left is None and node.right is None:
                    return minDepth
                # add the nodes to the queue for the level to be complete
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    findMinDepth(root)
