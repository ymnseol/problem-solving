# [1차] 프렌즈4블록

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><h2>프렌즈4블록</h2>

<p>블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".<br>
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.</p>

<p><img src="http://t1.kakaocdn.net/welcome2018/pang1.png" title="Friends 4 block!" alt="board map"><br>
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.</p>

<p><img src="http://t1.kakaocdn.net/welcome2018/pang2.png" title="Friends 4 block!" alt="board map"></p>

<p>블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.</p>

<p><img src="http://t1.kakaocdn.net/welcome2018/pang3.png" title="Friends 4 block!" alt="board map"></p>

<p>만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.<br>
<img src="http://t1.kakaocdn.net/welcome2018/pang4.png" title="Friends 4 block!" alt="board map"></p>

<p>위 초기 배치를 문자로 표시하면 아래와 같다.</p>
<div class="highlight"><pre class="codehilite"><code>TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
</code></pre></div>
<p>각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다</p>

<p>입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.</p>

<h3>입력 형식</h3>

<ul>
<li>입력으로 판의 높이 <code>m</code>, 폭 <code>n</code>과 판의 배치 정보 <code>board</code>가 들어온다.</li>
<li>2 ≦ <code>n</code>, <code>m</code> ≦ 30</li>
<li><code>board</code>는 길이 <code>n</code>인 문자열 <code>m</code>개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.</li>
</ul>

<h3>출력 형식</h3>

<p>입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.</p>

<h3>입출력 예제</h3>
<table class="table">
        <thead><tr>
<th>m</th>
<th>n</th>
<th>board</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>4</td>
<td>5</td>
<td>["CCBDE", "AAADE", "AAABF", "CCBBF"]</td>
<td>14</td>
</tr>
<tr>
<td>6</td>
<td>6</td>
<td>["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]</td>
<td>15</td>
</tr>
</tbody>
      </table>
<h3>예제에 대한 설명</h3>

<ul>
<li>입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.</li>
<li>입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.</li>
</ul>

<p><a href="http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/" target="_blank" rel="noopener">해설 보러가기</a></p>
</div>
    </div>

---

## 풀이

Deque를 활용합니다.

```Python
from collections import deque

class Board:
    def __init__(self, n_rows, n_cols, board):
        self.board = board
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_erased = 0
    
    def build(self):
        self.board = [list(row) for row in self.board]
        self.board = [deque([self.board[row][col] for row in range(self.n_rows)]) for col in range(self.n_cols)]
        self.n_rows, self.n_cols = self.n_cols, self.n_rows
    
    def check(self, row, col, target):
        if target:
            return sum([True for r in range(row, row + 2) for c in range(col, col + 2) if target == self.board[r][c]]) == 4
        return False
    
    def erase(self):
        to_erase = set()
        for row in range(self.n_rows - 1):
            for col in range(self.n_cols - 1):
                if self.check(row, col, self.board[row][col]):
                    to_erase.add((row, col))
                    to_erase.add((row, col + 1))
                    to_erase.add((row + 1, col))
                    to_erase.add((row + 1, col + 1))
        for row, col in to_erase:
            self.board[row][col] = ''
        self.n_erased += len(to_erase)
        return self.board
    
    def push_down(self):
        for i, col in enumerate(list(self.board)):
            for j, block in enumerate(list(col)):
                if not block:
                    del self.board[i][j]
                    self.board[i].appendleft('')
        return self.board
    
    def play_game(self):
        old_n_erased = self.n_erased
        self.erase()
        self.push_down()
        if self.n_erased == old_n_erased:
            return self.n_erased
        self.play_game()

def solution(m, n, board):
    game = Board(m, n, board)
    game.build()
    game.play_game()
    return game.n_erased
```

### 수행 과정

1. 주어진 판을 반시계 방향으로 90도 회전시킵니다. 원래 판의 열이 회전 후 리스트의 행이 됩니다. 리스트의 행을 모두 deque로 설정합니다.
2. 2×2 형태 중 왼쪽 위 블록을 기준으로 하여, 판에서 2×2 형태로 같은 블록이 4개가 붙어있는 경우를 모두 찾습니다. 조건을 만족하는 블록의 좌표를 저장합니다. 아래 조건을 만족시키기 위해 블록을 바로 지우지 않습니다.
   
   > 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

3. 저장된 좌표 블록 값을 ''로 바꾸어 지움 처리합니다.
4. 지운 블록의 왼쪽(판을 회전하기 전 위쪽) 블록들을 블록이 지워진 자리로 옮겨야 합니다. 2×2 형태를 만족하는 블록이 있는지 찾기 위해 deque의 길이를 균일하게 유지하는 것이 편리합니다. Deque마다 지움 처리된 블록이 있을 경우 deque에서 꺼내고, 길이 유지를 위해 ''를 head에 삽입합니다. 위 연산을 통해 블록을 왼쪽에서 오른쪽으로 밀 수 있습니다.
5. 더이상 지울 수 있는 블록이 없을 때까지 위 과정을 반복합니다.
