# coding: utf-8
# When to use: Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be O(W)O(W), where ‘W’ is the maximum number of nodes on any level.
# Example Problem: Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
# Solution/Algorithm:
