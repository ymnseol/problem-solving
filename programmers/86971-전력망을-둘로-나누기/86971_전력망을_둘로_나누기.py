# 프로그래머스 - 전력망을 둘로 나누기(86971)
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

class Graph:
    def __init__(self, n_vertices, edges):
        self.n_vertices = n_vertices
        self.edges = edges
        self.diff = self.n_vertices
    
    def dfs(self, s, g):
        stack = [s]
        visited = set()
        
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                for v in g[u]:
                    if v not in visited:
                        stack.append(v)
        return len(visited)
    
    def divide(self):
        for d in range(len(self.edges)):
            edges = [e for e in self.edges]
            edges.pop(d)
            graph = [[] for _ in range(self.n_vertices + 1)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            self.diff = min(self.diff, abs(2 * self.dfs(1, graph) - self.n_vertices))
            
    
def solution(n, wires):
    graph = Graph(n, wires)
    graph.divide()
    return graph.diff
