"""
Given the root of a binary tree, invert the tree, and return its root.
"""

import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invert_tree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root


class TestSolution(unittest.TestCase):

    def test1(self):
        solution = Solution()
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        inverted_root = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
        self.assertEqual(inverted_root.left.left.val, solution.invert_tree(root).left.left.val)
