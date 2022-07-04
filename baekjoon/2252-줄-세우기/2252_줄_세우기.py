# 백준 - 줄 세우기(2252)
# https://www.acmicpc.net/problem/2252

from collections import deque

class SimpleDirectedGraph:
    def __init__(self, n_vertices):
        self.adj_list = [[] for _ in range(n_vertices + 1)]
        self.indegree = [0 for _ in range(n_vertices + 1)]

    def insert(self, s, d):
        self.indegree[d] += 1
        self.adj_list[s].append(d)
    
    def topological_sort(self):
        order = []
        queue = deque()

        for v, i in enumerate(self.indegree):
            if v and not i:
                queue.append(v)
        
        while queue:
            u = queue.popleft()
            order.append(str(u))
            
            for n in self.adj_list[u]:
                self.indegree[n] -= 1
                if not self.indegree[n]:
                    queue.append(n)

        return ' '.join(order)

if __name__ == '__main__':
    N, M = map(int, input().split())

    graph = SimpleDirectedGraph(N)

    for i in range(M):
        s, d = map(int, input().split())
        graph.insert(s, d)

    print(graph.topological_sort())
