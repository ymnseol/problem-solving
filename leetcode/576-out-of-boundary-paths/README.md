# Out of Boundary Paths

<div class="content__u3I1 question-content__JfgR"><div><p>There is an <code>m x n</code> grid with a ball. The ball is initially at the position <code>[startRow, startColumn]</code>. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply <strong>at most</strong> <code>maxMove</code> moves to the ball.</p>

<p>Given the five integers <code>m</code>, <code>n</code>, <code>maxMove</code>, <code>startRow</code>, <code>startColumn</code>, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png" style="width: 500px; height: 296px;">
<pre><strong>Input:</strong> m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
<strong>Output:</strong> 6
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 293px;">
<pre><strong>Input:</strong> m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= maxMove &lt;= 50</code></li>
	<li><code>0 &lt;= startRow &lt; m</code></li>
	<li><code>0 &lt;= startColumn &lt; n</code></li>
</ul>
</div></div>

***

## Submitted solution
This uses the idea of BFS(Breadth First Search).
```Python
class Solution:
    def __init__(self):
        self.n_rows = -1
        self.n_cols = -1
    
    @cache
    def track(self, r: int, c: int, moves_left: int):
        if moves_left < 0:
            return 0
        elif (r < 0 or r >= self.n_rows) or (c < 0 or c >= self.n_cols):
            return 1
        else:
            return self.track(r - 1, c, moves_left - 1) + self.track(r + 1, c, moves_left - 1) + self.track(r, c - 1, moves_left - 1) + self.track(r, c + 1, moves_left - 1)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize
        self.n_rows = m
        self.n_cols = n

        return self.track(startRow, startColumn, maxMove) % 1000000007
```
### Improvement process
This uses DFS or BFS by modifying the concept of adjacent vertices.  
> You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary).

This chooses BFS

Every cell in the grid has exactly four adjacent cells. In the process of inserting adjacent vertices into the stack of DFS or queue of BFS, the top, bottom, left, and right cells of the corresponding cell may be inserted as adjacent vertices.  

Additionally, this must consider the number of moves.  
At first, this tries to check whether the number of moves exceeds the given limit by calculating the L1 distance.  

```Python
from collections import deque

class Solution:
    def __init__(self):
        self.n_rows = -1
        self.n_cols = -1
        self.max_move = -1

    def in_grid(self, u: tuple):
        return 0 <= u[0] < self.n_rows and 0 <= u[1] < self.n_cols
    
    def top(self, u: tuple):
        return (u[0] - 1, u[1])
    
    def bottom(self, u: tuple):
        return (u[0] + 1, u[1])
    
    def left(self, u: tuple):
        return (u[0], u[1] - 1)
    
    def right(self, u: tuple):
        return (u[0], u[1] + 1)

    def neighbors(self, u: tuple):
        return [self.top(u), self.bottom(u), self.left(u), self.right(u)]
    
    def no_moves_left(self, u: tuple, v: tuple):
        return abs(u[0] - v[0]) + abs(u[1] - v[1]) >= self.max_move

    @cache
    def bfs(self, s):
        n_paths = 0
        visited = {s}
        queue = deque([s])

        while queue:
            u = queue.popleft()
            if self.no_moves_left(s, u):
                continue

            for v in self.neighbors(u):
                if v not in visited:
                    visited.add(v)
                    if self.in_grid(v):
                        queue.append(v)
                    else:
                        n_paths += 1
        
        return n_paths

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize
        self.n_rows = m
        self.n_cols = n
        self.max_move = maxMove

        return self.bfs((startRow, startColumn)) % 1000000007

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize
        self.n_rows = m
        self.n_cols = n
        self.max_move = maxMove

        return self.bfs((startRow, startColumn)) % 1000000007
```
But, L1 distance between the source vertex and the current vertex does not represent the expected number of moves in the following case:

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 293px;">
<pre><strong>Input:</strong> m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
<strong>Output:</strong> 12
</pre>

To count the number of moves properly, this implements the modified BFS using the recursion:
```Python
class Solution:
    def __init__(self):
        self.n_rows = -1
        self.n_cols = -1
    
    @cache
    def track(self, r: int, c: int, moves_left: int):
        if moves_left < 0:
            return 0
        elif (r < 0 or r >= self.n_rows) or (c < 0 or c >= self.n_cols):
            return 1
        else:
            return self.track(r - 1, c, moves_left - 1) + self.track(r + 1, c, moves_left - 1) + self.track(r, c - 1, moves_left - 1) + self.track(r, c + 1, moves_left - 1)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize
        self.n_rows = m
        self.n_cols = n

        return self.track(startRow, startColumn, maxMove) % 1000000007
```
### To-do
1. The recursive solution is intuitive, but it consumes too long time without caching.  
How can this count the number of moves without using the recursion?  
2. Is there any mathematical way to count the number of paths?