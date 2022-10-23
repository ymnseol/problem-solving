# LeetCode - Regular Expression Matching(33)
# https://leetcode.com/problems/regular-expression-matching/

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if re.fullmatch(p, s) else False
