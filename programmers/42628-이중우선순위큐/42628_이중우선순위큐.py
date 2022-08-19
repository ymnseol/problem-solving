# 프로그래머스 - 이중우선순위큐(42628)
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    max_pq = []
    min_pq = []
    popped = set()
    for i, op in enumerate(operations):
        if op[0] == 'I':
            heapq.heappush(max_pq, (-int(op[2:]), i))
            heapq.heappush(min_pq, (int(op[2:]), i))
        elif op == 'D -1':
            while min_pq and min_pq[0][1] in popped:
                heapq.heappop(min_pq)
            if min_pq:
                popped.add(heapq.heappop(min_pq)[1])
        elif op == 'D 1':
            while max_pq and max_pq[0][1] in popped:
                heapq.heappop(max_pq)
            if max_pq:
                popped.add(heapq.heappop(max_pq)[1])
    while max_pq and max_pq[0][1] in popped:
        heapq.heappop(max_pq)
    while min_pq and min_pq[0][1] in popped:
        heapq.heappop(min_pq)
    if max_pq and min_pq:
        return [-max_pq[0][0], min_pq[0][0]]
    return [0, 0]
    