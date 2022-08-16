# 프로그래머스 - 네트워크(43162)
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.graph = [[] for _ in range(self.n_vertices)]
        self.visited = set()
    
    def build(self, edges):
        for i, edge in enumerate(edges):
            for j, v in enumerate(edge):
                if v and i != j:
                    self.graph[i].append(j)
        
    def bfs(self, s):
        queue = deque([s])
        
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if v not in self.visited:
                    self.visited.add(v)
                    queue.append(v)
        
        return True

def solution(n, computers):
    answer = 0
    graph = Graph(n)
    graph.build(computers)
    for i in range(n):
        if i not in graph.visited:
            graph.bfs(i)
            answer += 1
    return answer
