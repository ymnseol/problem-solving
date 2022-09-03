# 프로그래머스 - 등산코스 정하기(118669)
# https://school.programmers.co.kr/learn/courses/30/lessons/118669

from collections import defaultdict, deque

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    
    # Build a graph
    graph = defaultdict(set)
    for u, v, cost in paths:
        graph[u].add((cost, v))
        graph[v].add((cost, u))
    
    # Implement BFS
    intensity = [10000000] * (n + 1)
    pq = deque([])
    
    for u in gates:
        intensity[u] = 0
        pq.append((0, u))
    
    while pq:
        i, u = pq.popleft()
        
        if u in summits or i > intensity[u]:
            continue
        
        for j, v in graph[u]:
            new_j = max(i, j)
            if new_j < intensity[v]:
                intensity[v] = new_j
                pq.append((new_j, v))
    
    i, u = min([(intensity[u], u) for u in summits])
    return [u, i]
