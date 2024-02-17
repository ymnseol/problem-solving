# 프로그래머스 - 괄호 회전하기(76502)
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque


def solution(s):
    answer = 0
    bracket_pairs = {"[": "]", "{": "}", "(": ")"}
    for offset in range(len(s)):
        stack = []
        brackets = deque(s[offset:] + s[:offset])
        for bracket in brackets:
            stack.append(bracket)
            if len(stack) > 1 and bracket_pairs.get(stack[-2]) == stack[-1]:
                del stack[-2:]
        if not stack:
            answer += 1
    return answer
