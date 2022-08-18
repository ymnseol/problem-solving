# 프로그래머스 - 합승 택시 요금(72413)
# https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq

class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.graph = [[] for _ in range(self.n_vertices + 1)]
        
    def build(self, edges):
        for u, v, cost in edges:
            self.graph[u].append((cost, v))
            self.graph[v].append((cost, u))
    
    def dijkstra(self, s, d):
        dist = [float('inf')] * (self.n_vertices + 1)
        dist[s] = 0
        pq = [(dist[s], s)]
        
        while pq:
            curr_d, curr_v = heapq.heappop(pq)
            if dist[curr_v] < curr_d:
                continue
            for next_d, next_v in self.graph[curr_v]:
                new_d = curr_d + next_d
                if new_d < dist[next_v]:
                    dist[next_v] = new_d
                    heapq.heappush(pq, (new_d, next_v))
        return dist[d]

def solution(n, s, a, b, fares):
    graph = Graph(n)
    graph.build(fares)
    cost = graph.dijkstra(s, a) + graph.dijkstra(s, b)
    for i in range(1, n + 1):
        cost = min(cost, graph.dijkstra(s, i) + graph.dijkstra(i, a) + graph.dijkstra(i, b))
    return cost
