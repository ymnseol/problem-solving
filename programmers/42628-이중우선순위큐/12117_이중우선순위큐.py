# 프로그래머스 - 이중우선순위큐(42628)
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    max_pq = []
    min_pq = []
    popped = []
    
    for i, o in enumerate(operations):
        if o[0] == "I":
            max_pq.append((-int(o[2:]), i))
            min_pq.append((int(o[2:]), i))
        elif o == "D 1":
            heapq.heapify(max_pq)
            
            while max_pq and max_pq[0][1] in popped:
                heapq.heappop(max_pq)
            
            if max_pq:
                popped.append(heapq.heappop(max_pq)[1])
        elif o == "D -1":
            heapq.heapify(min_pq)
            
            while min_pq and min_pq[0][1] in popped:
                heapq.heappop(min_pq)
            
            if min_pq:
                popped.append(heapq.heappop(min_pq)[1])
    
    while max_pq and max_pq[0][1] in popped:
        heapq.heappop(max_pq)
        
    while min_pq and min_pq[0][1] in popped:
        heapq.heappop(min_pq)
    
    heapq.heapify(max_pq)
    heapq.heapify(min_pq)
    
    if min_pq or max_pq:
        return [-max_pq[0][0], min_pq[0][0]]
    else:
        return [0, 0]