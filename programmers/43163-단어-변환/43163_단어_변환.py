# 프로그래머스 - 단어 변환(43163)
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

import heapq

class Graph:
    def __init__(self, dest):
        self.graph = dict()
        self.dest = dest
    
    def build(self, s, d, vs):
        self.graph[s] = []
        for v in vs:
            self.graph[v] = []
        for v in vs:
            for k in self.graph.keys():
                if sum([1 for i in range(len(v)) if v[i] != k[i]]) == 1:
                    self.graph[k].append((1, v))
        self.graph[d] = []
    
    def dijkstra(self, s):
        dist = dict()
        for k in self.graph.keys():
            dist[k] = float('inf')
        dist[s] = 0
        pq = [(dist[s], s)]
        
        while pq:
            d, v = heapq.heappop(pq)
            if dist[v] < d:
                continue
            for next_d, next_v in self.graph[v]:
                new_d = next_d + d
                if new_d < dist[next_v]:
                    dist[next_v] = new_d
                    heapq.heappush(pq, (new_d, next_v))
        return dist[self.dest]

def solution(begin, target, words):
    if target not in words:
        return 0
    graph = Graph(target)
    graph.build(begin, target, words)
    return graph.dijkstra(begin)
