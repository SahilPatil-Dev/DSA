"""
Problem: Group Anagrams
Platform: LeetCode / NeetCode
Topic: Hashing, Strings

Approach 1: Sorting (Simple)
- Sort each word and use it as key
Time Complexity: O(n * k log k)
Space Complexity: O(n)

Approach 2: Character Count (Optimal)
- Use 26-length frequency array as key
Time Complexity: O(n * k)
Space Complexity: O(n)

Approach 3: defaultdict (Clean Pythonic)
- Same as above but cleaner using defaultdict
"""

from typing import List
from collections import defaultdict


class Solution:

    # Approach 1: Sorting
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())

    # Approach 2: Character Count (Optimal)
    def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())

    # Approach 3: defaultdict (Cleanest)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())