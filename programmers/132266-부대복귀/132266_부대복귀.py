# 프로그래머스 - 부대복귀(132266)
# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque


class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.graph = [[] for _ in range(self.n_vertices + 1)]

    def build(self, edges):
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def bfs(self, s):
        queue = deque([s])
        dist = [0] * (self.n_vertices + 1)
        dist[s] = 1

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if dist[v]:
                    continue
                queue.append(v)
                dist[v] = dist[u] + 1

        return dist


def solution(n, roads, sources, destination):
    graph = Graph(n)
    graph.build(roads)
    counts = graph.bfs(destination)
    return [counts[s] - 1 if counts[s] else -1 for s in sources]
