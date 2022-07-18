# 프로그래머스 - 짝지어 제거하기(12973)
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    if len(s) % 2 == 1: return 0
    
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return 0 if stack else 1
