# LeetCode - Top K Frequent Elements(347)
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [n for n, _ in counter.most_common(k)]
