# LeetCode - Longest Substring Without Repeating Characters(3)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        left = right = 0
        max_len = 0
        
        while right < len(s):
            if s[right] in curr:
                curr.remove(s[left])
                max_len = max(max_len, right - left)
                left += 1
            else:
                curr.add(s[right])
                right += 1
        
        return max(max_len, right - left)
