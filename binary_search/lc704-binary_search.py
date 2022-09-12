"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
import unittest


class Solution(object):
    @staticmethod
    def search(nums, target):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


# Testing
class TestSolution(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual(4, solution.search([-1, 0, 3, 5, 9, 12], 9))

    def test2(self):
        solution = Solution()
        self.assertEqual(-1, solution.search([-1, 0, 3, 5, 9, 12], 2))


if __name__ == '__main__':
    unittest.main()
