# 프로그래머스 - 빛의 경로 사이클(86052)
# https://school.programmers.co.kr/learn/courses/30/lessons/86052#

class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self.visited = set()
        # 0: E, 1: W, 2: S, 3: N
        self.sr = [0, 0, 1, -1]
        self.sc = [1, -1, 0, 0]
        self.lr = [-1, 1, 0, 0]
        self.lc = [0, 0, 1, -1]
        self.ld = [3, 2, 0, 1]
        self.rr = [1, -1, 0, 0]
        self.rc = [0, 0, -1, 1]
        self.rd = [2, 3, 1, 0]
    
    def dfs(self, source_r, source_c, starting_dir):
        cnt = 0
        stack = [(source_r, source_c, starting_dir)]

        while stack:
            r, c, d = stack.pop()
            if cnt and (r, c, d) == (source_r, source_c, starting_dir):
                return cnt
            if (r, c, d) in self.visited:
                return 0

            self.visited.add((r, c, d))
            
            if self.grid[r][c] == 'S':
                next_r = (r + self.sr[d]) % self.n_rows
                next_c = (c + self.sc[d]) % self.n_cols
                next_d = d
            elif self.grid[r][c] == 'L':
                next_r = (r + self.lr[d]) % self.n_rows
                next_c = (c + self.lc[d]) % self.n_cols
                next_d = self.ld[d]
            else: # self.grid[r][c] == 'R':
                next_r = (r + self.rr[d]) % self.n_rows
                next_c = (c + self.rc[d]) % self.n_cols
                next_d = self.rd[d]
                
            stack.append((next_r, next_c, next_d))
            cnt += 1
        return 0
    
def solution(grid):
    answer = []
    graph = Graph(grid)
    for r in range(graph.n_rows):
        for c in range(graph.n_cols):
            for d in range(4):
                cnt = graph.dfs(r, c, d)
                if cnt:
                    answer.append(cnt)
    
    return sorted(answer)
