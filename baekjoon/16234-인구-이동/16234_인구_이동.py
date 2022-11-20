import sys
from collections import deque
from typing import List

class Graph:
    def __init__(self, populations: List[List], lower: int, upper: int):
        self.populations = populations
        self.n_rows = len(populations)
        self.lower = lower
        self.upper = upper
        self.visited = [[False] * self.n_rows for _ in range(self.n_rows)]
        self.cnt = 0
        self.need_more_traversals = True

    def reset_visited(self) -> None:
        self.visited = [[False] * self.n_rows for _ in range(self.n_rows)]
    
    def _bfs(self, sr: int, sc: int) -> bool:
        queue = deque([(sr, sc)])
        self.visited[sr][sc] = True
        united_nations = set()
        sum_of_populations = self.populations[sr][sc]

        drs = (-1, 0, 0, 1) # N, E, W, S
        dcs = (0, 1, -1, 0) # N, E, W, S

        while queue:
            curr_r, curr_c = queue.popleft()
            curr_population = self.populations[curr_r][curr_c]

            for dr, dc in zip(drs, dcs):
                new_r, new_c = curr_r + dr, curr_c + dc
                if not ((0 <= new_r < self.n_rows) and (0 <= new_c < self.n_rows)):
                    continue
                if self.visited[new_r][new_c]:
                    continue
                if self.lower <= abs(curr_population - self.populations[new_r][new_c]) <= self.upper:
                    queue.append((new_r, new_c))
                    united_nations.add((new_r, new_c))
                    sum_of_populations += self.populations[new_r][new_c]
                    self.visited[new_r][new_c] = True

        if not united_nations:
            return False
        
        new_population = sum_of_populations // (len(united_nations) + 1)
        self.populations[sr][sc] = new_population
        for r, c in united_nations:
            self.populations[r][c] = new_population
        return united_nations
    
    def bfs(self) -> None:
        new_union = False
        for r in range(self.n_rows):
            for c in range(self.n_rows):
                if self.visited[r][c]:
                    continue
                if self._bfs(r, c):
                    new_union = True
        if not new_union:
            self.need_more_traversals = False
            return
        self.reset_visited()
        self.cnt += 1


if __name__ == '__main__':
    N, L, R = list(map(int, sys.stdin.readline().split()))
    A = []
    for _ in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))
    graph = Graph(populations=A, lower=L, upper=R)
    while graph.need_more_traversals:
        graph.bfs()
    print(graph.cnt)
