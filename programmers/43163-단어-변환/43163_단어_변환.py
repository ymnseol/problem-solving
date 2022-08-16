# 프로그래머스 - 단어 변환(43163)
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

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
                    self.graph[k].append(v)
        self.graph[d] = []
    
    def bfs(self, s):
        dist = dict()
        for k in self.graph.keys():
            dist[k] = float('inf')
        dist[s] = 0
        queue = deque([s])
        
        while queue:
            u = queue.popleft()
            if u == self.dest:
                return dist[self.dest]
            for v in self.graph[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    queue.append(v)

def solution(begin, target, words):
    if target not in words:
        return 0
    graph = Graph(target)
    graph.build(begin, target, words)
    return graph.bfs(begin)
