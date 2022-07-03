# 백준 - DFS와 BFS(1260)
# https://www.acmicpc.net/problem/1260

from collections import deque

class SimpleGraph:
    def __init__(self):
        self.adj_list = dict()
        self.visited = set()
    
    def insert(self, e):
        if e[0] in self.adj_list:
            self.adj_list[e[0]].append(e[1])
        else:
            self.adj_list[e[0]] = [e[1]]
        if e[1] in self.adj_list:
            self.adj_list[e[1]].append(e[0])
        else:
            self.adj_list[e[1]] = [e[0]]
    
    def sort_neighbors(self):
        for k, _ in self.adj_list.items():
            self.adj_list[k].sort()
    
    def clean(self):
        self.visited = set()
    
    def dfs(self, s):
        print(s, end=' ')

        if s not in self.adj_list:
            return

        self.visited.add(s)
        for v in self.adj_list[s]:
            if v not in self.visited:
                self.dfs(v)
    
    def bfs(self, s):
        self.visited.add(s)
        queue = deque([s])

        while queue:
            u = queue.popleft()
            print(u, end=' ')
            if u not in self.adj_list:
                return
            for v in self.adj_list[u]:
                if v not in self.visited:
                    self.visited.add(v)
                    queue.append(v)

if __name__ == '__main__':
    N, M, V = map(int, input().split())
    graph = SimpleGraph()
    for _ in range(M):
        u, v = map(int, input().split())
        graph.insert((u, v))
    graph.sort_neighbors()
    graph.dfs(V)
    graph.clean()
    print()
    graph.bfs(V)
