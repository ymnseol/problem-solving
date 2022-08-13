# 프로그래머스 - 프린터(42587)
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    priorities = deque([(p, i) for i, p in enumerate(priorities)])
    cnt = 0
    while priorities:
        p, i = priorities[0]
        if p == max(priorities)[0]:
            priorities.popleft()
            cnt += 1
            if i == location:
                return cnt
        else:
            priorities.popleft()
            priorities.append((p, i))
