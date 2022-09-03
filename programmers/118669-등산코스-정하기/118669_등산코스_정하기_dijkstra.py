# 프로그래머스 - 등산코스 정하기(118669)
# https://school.programmers.co.kr/learn/courses/30/lessons/118669

import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    
    # Build a graph
    graph = defaultdict(set)
    for u, v, cost in paths:
        graph[u].add((cost, v))
        graph[v].add((cost, u))
    
    # Implement Dijkstra's algorithm
    intensity = [10000000] * (n + 1)
    pq = []
    
    for u in gates:
        intensity[u] = 0
        pq.append((0, u))
    
    while pq:
        i, u = heapq.heappop(pq)
        
        if u in summits or i > intensity[u]:
            continue
        
        for j, v in graph[u]:
            new_j = max(i, j)
            if new_j < intensity[v]:
                intensity[v] = new_j
                heapq.heappush(pq, (new_j, v))
    
    i, u = min([(intensity[u], u) for u in summits])
    return [u, i]
