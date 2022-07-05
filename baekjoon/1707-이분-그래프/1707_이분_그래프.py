# 백준 - 이분 그래프(1707)
# https://www.acmicpc.net/problem/1707

from collections import deque

class SimpleGraph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_list = [[] for _ in range(self.n_vertices + 1)]
        self.color = ['' for _ in range(self.n_vertices + 1)]
        self.visited = set()
    
    def insert(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def _bfs(self, s):
        color = 'R'

        self.visited.add(s)
        self.color[s] = 'B'
        queue = deque([s])

        while queue:
            u = queue.popleft()
            
            if self.color[u] == 'B':
                color = 'R'
            else:
                color = 'B'

            for v in self.adj_list[u]:
                if self.color[v] == self.color[u]:
                        return False
                self.color[v] = color
                if v not in self.visited:
                    self.visited.add(v)
                    queue.append(v)
            
        return True
    
    def bfs(self):
        for v in range(1, self.n_vertices + 1):
            if v not in self.visited:
                if not self._bfs(v):
                    return False
        return True

if __name__ == '__main__':
    K = int(input()) # K: The number of test cases

    for i in range(K):
        V, E = map(int, input().split()) # V: The number of vertices, E: The number of edges

        graph = SimpleGraph(V)

        for j in range(E):
            u, v = map(int, input().split())
            graph.insert(u, v)
        
        if graph.bfs():
            print('YES')
        else:
            print('NO')
