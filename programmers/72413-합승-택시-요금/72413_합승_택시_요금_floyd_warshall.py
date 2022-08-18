# 프로그래머스 - 합승 택시 요금(72413)
# https://school.programmers.co.kr/learn/courses/30/lessons/72413

class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.graph = [[float('inf')] * (self.n_vertices + 1) for _ in range(self.n_vertices + 1)]
        
    def build(self, edges):
        for u, v, cost in edges:
            self.graph[u][u] = 0
            self.graph[v][v] = 0
            self.graph[u][v] = cost
            self.graph[v][u] = cost
    
    def floyd_warshall(self):
        for k in range(1, self.n_vertices + 1):
            for i in range(1, self.n_vertices + 1):
                for j in range(1, self.n_vertices + 1):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

def solution(n, s, a, b, fares):
    graph = Graph(n)
    graph.build(fares)
    graph.floyd_warshall()
    cost = graph.graph[s][a] + graph.graph[s][b]
    for i in range(1, n + 1):
        cost = min(cost, graph.graph[s][i] + graph.graph[i][a] + graph.graph[i][b])
    return cost
