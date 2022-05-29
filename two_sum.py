import unittest
from typing import List, Dict


class Solution:
    @staticmethod
    def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
        for x_dx, x in enumerate(nums):
            for y_dx in range(x_dx + 1, len(nums)):
                y = nums[y_dx]
                if x + y == target:
                    return [x_dx, y_dx]

    @staticmethod
    def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
        store: Dict[int, int] = {}
        for x_dx, x in enumerate(nums):
            seek = target - x
            if seek in store:
                return [store.get(seek), x_dx]
            store[x] = x_dx


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(Solution.two_sum_bruteforce([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution.two_sum_bruteforce([3, 2, 4], 6), [1, 2])
        self.assertEqual(Solution.two_sum_bruteforce([3, 3], 6), [0, 1])

        self.assertEqual(Solution.two_sum_hashmap([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution.two_sum_hashmap([3, 2, 4], 6), [1, 2])
        self.assertEqual(Solution.two_sum_hashmap([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
