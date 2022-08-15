# 프로그래머스 - 야근 지수(12927)
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    max_pq = [-w for w in works]
    heapq.heapify(max_pq)
    for _ in range(n):
        top = heapq.heappop(max_pq)
        top += 1
        heapq.heappush(max_pq, top)
    return sum([n ** 2 for n in max_pq])
