"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
"""

import unittest
from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def max_depth_recursive_dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return 1 + max(self.max_depth_recursive_dfs(root.left), self.max_depth_recursive_dfs(root.right))

    def max_depth_bfs(self, root: Optional[TreeNode]):
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


class TestSolution(unittest.TestCase):

    def test1(self):
        solution = Solution()
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(3, solution.max_depth_recursive_dfs(root))
        self.assertEqual(3, solution.max_depth_bfs(root))
