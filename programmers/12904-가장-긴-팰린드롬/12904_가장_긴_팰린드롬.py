# 프로그래머스 - 가장 긴 팰린드롬(12904)
# https://school.programmers.co.kr/learn/courses/30/lessons/12904/

def solution(s):
    for l in range(len(s) - 1, -1, -1):
        left, right = 0, l
        while right < len(s):
            if s[left:right + 1] != s[left:right+1][::-1]:
                left += 1
                right += 1
            else:
                return l + 1
