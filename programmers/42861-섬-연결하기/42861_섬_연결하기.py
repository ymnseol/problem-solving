# 프로그래머스 - 섬 연결하기(42861)
# https://school.programmers.co.kr/learn/courses/30/lessons/42861

class Graph:
    def __init__(self, n_vertices, edges):
        self.root = [v for v in range(n_vertices)]
        self.edges = edges
    
    def find(self, v):
        if v == self.root[v]:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.root[root_v] = root_u
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def min_cost(self):
        cost = 0
        for c, u, v in self.edges:
            if not self.connected(u, v):
                self.union(u, v)
                cost += c
        return cost

def solution(n, costs):
    costs = sorted([[c, s, d]for s, d, c in costs])
    graph = Graph(n, costs)
    return graph.min_cost()
