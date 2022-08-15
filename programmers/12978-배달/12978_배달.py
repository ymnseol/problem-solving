# 프로그래머스 - 배달(12978)
# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq

class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.graph = [[] for _ in range(self.n_vertices + 1)]
        
    def build(self, edges): 
        for u, v, c in edges:
            self.graph[u].append((c, v))
            self.graph[v].append((c, u))

    def dijkstra(self, s):
        dist = [float('inf')] * (self.n_vertices + 1)
        dist[s] = 0
        pq = []
        heapq.heappush(pq, (dist[s], s))
        
        while pq:
            d, v = heapq.heappop(pq)
            if dist[v] < d:
                continue
            for next_d, next_v in self.graph[v]:
                new_d = d + next_d
                if new_d < dist[next_v]:
                    dist[next_v] = new_d
                    heapq.heappush(pq, (new_d, next_v))
        return dist

def solution(N, road, K):
    answer = []
    graph = Graph(N)
    graph.build(road)
    for i, c in enumerate(graph.dijkstra(1)):
        if c <= K:
            answer.append(i)
    return len(answer)
