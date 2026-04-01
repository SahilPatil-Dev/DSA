"""
Problem: Valid Anagram
Platform: LeetCode / NeetCode
Topic: Hashing, Strings

Approach:
- Count frequency of characters in string `s`
- Decrease frequency using string `t`
- If any count becomes negative → not an anagram
- If all checks pass → valid anagram

Time Complexity: O(n)
Space Complexity: O(1)  # assuming fixed character set (e.g., lowercase letters)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False

        return True