"""
Problem: Top K Frequent Elements
Platform: LeetCode / NeetCode
Topic: Arrays, Hashing, Heap, Bucket Sort

Approach 1: Sorting
- Count frequency and sort by frequency
Time: O(n log n)
Space: O(n)

Approach 2: Min Heap
- Keep top k elements using heap
Time: O(n log k)
Space: O(n)

Approach 3: Bucket Sort (Optimal)
- Use frequency buckets
Time: O(n)
Space: O(n)
"""

from typing import List
from collections import Counter
import heapq


class Solution:

    # 🔹 Approach 1: Sorting
    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]

    # 🔹 Approach 2: Min Heap
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]

    # 🔹 Approach 3: Bucket Sort (Optimal)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result