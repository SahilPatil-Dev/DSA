"""
Problem: Two Sum
Platform: LeetCode / NeetCode
Topic: Arrays, Hashing

Approach:
- Use hashmap to store number → index
- For each element, calculate complement (target - num)
- If complement exists in map → return indices

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in num_map:
                return [num_map[needed], i]

            num_map[num] = i

        return [-1, -1]