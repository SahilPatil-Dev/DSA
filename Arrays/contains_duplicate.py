"""
Problem: Contains Duplicate
Platform: NeetCode / LeetCode
Topic: Arrays, Hashing

Approach 1: Set Length Comparison
Time: O(n)
Space: O(n)

Approach 2: Hash Set
Time: O(n)
Space: O(n)
"""

from typing import List

class Solution:

    def hasDuplicate_set_len(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def hasDuplicate_hash(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

