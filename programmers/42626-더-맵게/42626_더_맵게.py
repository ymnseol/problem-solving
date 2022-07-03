# 프로그래머스 - 더 맵게(42626)
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap) # min heapify
    
    cnt = 0
    
    while len(heap) > 1:
        cnt += 1
        first_min = heapq.heappop(heap)
        second_min = heapq.heappop(heap)
        
        new_scale = first_min + second_min * 2
        heapq.heappush(heap, new_scale)
        
        if heap[0] >= K:
            return cnt
    
    return -1
    