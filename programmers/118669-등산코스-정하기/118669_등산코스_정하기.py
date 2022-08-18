# 프로그래머스 - 등산코스 정하기(118669)
# https://school.programmers.co.kr/learn/courses/30/lessons/118669

import heapq

class Graph:
    def __init__(self, n_vertices, gates, summits):
        self.n_vertices = n_vertices
        self.graph = [[] for _ in range(self.n_vertices + 1)]
        self.gates = set(gates)
        self.summits = set(summits)
    
    def build(self, edges):
        for u, v, cost in edges:
            ug = u in self.gates
            vg = v in self.gates
            us = u in self.summits
            vs = v in self.summits
            if ug and vg:
                continue
            elif us and vs:
                continue
            elif ug and not vg:
                self.graph[u].append((cost, v))
            elif vg and not ug:
                self.graph[v].append((cost, u))
            elif us and not vs:
                self.graph[v].append((cost, u))
            elif vs and not us:
                self.graph[u].append((cost, v))
            else:
                self.graph[u].append((cost, v))
                self.graph[v].append((cost, u))
    
    def dijkstra(self):
        intensity = [0 if i in self.gates else float('inf') for i in range(self.n_vertices + 1)]
        pq = [(0, g) for g in self.gates]

        while pq:
            _, curr_v = heapq.heappop(pq)
            for next_d, next_v in self.graph[curr_v]:
                new_i = max(intensity[curr_v], next_d)
                if new_i < intensity[next_v]:
                    intensity[next_v] = new_i
                    heapq.heappush(pq, (next_d, next_v))
                
        return min([(intensity[s], s) for s in self.summits])[::-1]

def solution(n, paths, gates, summits):
    graph = Graph(n, gates, summits)
    graph.build(paths)
    return graph.dijkstra()
