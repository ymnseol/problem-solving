# 프로그래머스 - 가장 먼 노드(49189)
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    g = [[] for _ in range(n + 1)]
    
    for s, d in edge: 
        g[s].append(d)
        g[d].append(s)
    
    queue = deque([1])
    dist = [0] * (n + 1)
    
    while queue:
        u = queue.popleft()
        dist[u] += 1
        for v in g[u]:
            if not dist[v]:
                dist[v] = dist[u] + 1
                queue.append(v)
    
    return dist.count(max(dist))
