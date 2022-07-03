# 백준 - 적록색약(10026)
# https://www.acmicpc.net/problem/10026

from collections import deque
from time import sleep

class SimpleGraph:
    def __init__(self, side_len, grid):
        self.side_len = side_len
        self.grid = grid
        self.visited = set()
        self.n_parts = 0

    def _bfs(self, s):
        self.visited.add(s)
        queue = deque([s])
        sc = s[2]

        while queue:
            ux, uy, _ = queue.popleft()
            
            l = self.grid[max(ux - 1, 0)][uy]
            r = self.grid[min(ux + 1, self.side_len - 1)][uy]
            t = self.grid[ux][max(uy - 1, 0)]
            b = self.grid[ux][min(uy + 1, self.side_len - 1)]
            
            ns = [l, r, t, b]

            for n in ns:
                if n not in self.visited and (n[0], n[1]) != (ux, uy) and n[2] == sc:
                    self.visited.add(n)
                    queue.append(n)
        
        self.n_parts += 1
    
    def bfs(self):
        for vs in self.grid:
            for v in vs:
                if v not in self.visited:
                    self._bfs(v)
        
if __name__ == '__main__':
    N = int(input())

    n_grid = []
    p_grid = []
    
    for i in range(N):
        row = input()
        n_temp = []
        p_temp = []
        for j in range(N):
            n_temp.append((i, j, row[j]))
            if row[j] == 'G':
                p_temp.append((i, j, 'R'))
            else:
                p_temp.append((i, j, row[j]))
        n_grid.append(n_temp)
        p_grid.append(p_temp)
    
    n_graph = SimpleGraph(N, n_grid)
    p_graph = SimpleGraph(N, p_grid)

    n_graph.bfs()
    p_graph.bfs()

    print(n_graph.n_parts, p_graph.n_parts)
