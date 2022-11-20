# LeetCode - Longest Consecutive Sequence(128)
# https://leetcode.com/problems/longest-consecutive-sequence

from collections import Counter
from typing import List

class Graph:
    def __init__(self, nums):
        self.pos = {n: i for i, n in enumerate(nums)}
        self.root = [i for i in range(len(nums))]
    
    def find(self, v):
        if v == self.root[v]:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]
    
    def union(self, u, v):
        root_u = self.find(self.pos[u])
        root_v = self.find(self.pos[v])
        if root_u != root_v:
            self.root[root_v] = root_u


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        graph = Graph(nums)
        for n in nums:
            if graph.pos.get(n - 1) is not None: graph.union(n - 1, n)
        for n in nums:
            if graph.pos.get(n - 1) is not None: graph.union(n - 1, n)
        return Counter(graph.root).most_common(1)[0][1]
        