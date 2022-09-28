import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            dfs(idx + 1)

            subset.pop()
            dfs(idx + 1)

        dfs(0)
        return res


class TestSolution(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual([[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []], solution.subsets([1, 2, 3]))

    def test2(self):
        solution = Solution()
        self.assertEqual([[0], []], solution.subsets([0]))
