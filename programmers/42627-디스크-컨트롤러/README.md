# 디스크 컨트롤러

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.</p>

<p>예를들어</p>
<div class="highlight"><pre class="codehilite"><code>- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
</code></pre></div>
<p>와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.<br>
  <img src="https://grepp-programmers.s3.amazonaws.com/files/production/b68eb5cec6/38dc6a53-2d21-4c72-90ac-f059729c51d5.png" title="" alt="Screen Shot 2018-09-13 at 6.34.58 PM.png"></p>

<p>한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.<br>
  <img src="https://grepp-programmers.s3.amazonaws.com/files/production/5e677b4646/90b91fde-cac4-42c1-98b8-8f8431c52dcf.png" title="" alt="Screen Shot 2018-09-13 at 6.38.52 PM.png"></p>
<div class="highlight"><pre class="codehilite"><code>- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
</code></pre></div>
<p>이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.</p>

<p>하지만 A → C → B 순서대로 처리하면<br>
  <img src="https://grepp-programmers.s3.amazonaws.com/files/production/9eb7c5a6f1/a6cff04d-86bb-4b5b-98bf-6359158940ac.png" title="" alt="Screen Shot 2018-09-13 at 6.41.42 PM.png"></p>
<div class="highlight"><pre class="codehilite"><code>- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
</code></pre></div>
<p>이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.</p>

<p>각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)</p>

<h5>제한 사항</h5>

<ul>
<li>jobs의 길이는 1 이상 500 이하입니다.</li>
<li>jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.</li>
<li>각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.</li>
<li>각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.</li>
<li>하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>jobs</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[[0, 3], [1, 9], [2, 6]]</td>
<td>9</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>문제에 주어진 예와 같습니다.</p>

<ul>
<li>0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.</li>
<li>1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.</li>
<li>2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.</li>
</ul>
</div>
    </div>

***

## 풀이

Heap을 사용합니다.
```Python
import heapq

def solution(jobs):
    visited = set()
    jobs.sort()
    pq = [[jobs[0][1], jobs[0][0]]]
    curr_time = jobs[0][0]
    total_time = 0
    
    while pq:
        required_time, start_time = heapq.heappop(pq)
        visited.add((start_time, required_time))
        total_time += curr_time + required_time - start_time
        if len(visited) < len(jobs):
            curr_time = max(curr_time + required_time, jobs[len(visited)][0])
        else:
            curr_time += required_time
        pq = [[r, s] for s, r in jobs if s <= curr_time and (s, r) not in visited]
        heapq.heapify(pq)
    return total_time // len(jobs)
```

### 수행 과정

해당 시점에서 이미 요청이 되었거나 요청이 되는 작업 중 작업의 소요 시간이 가장 짧은 작업을 수행하면 됩니다.

1. 현재 시점에서 이미 요청이 되었거나 요청이 되는 작업으로 최소 힙을 구성합니다.
2. 작업의 소요 시간이 가장 짧은 작업을 수행합니다. 해당 작업 요청 후 대기 시간과 작업의 소요 시간을 합친 시간만큼이 해당 작업을 위한 총 소요 시간입니다.
3. 다음 요청이 들어오는 시점을 기준으로 위 작업을 반복합니다.
4. 모든 작업의 소요 시간을 합한 값을 작업의 개수로 나누어 평균 소요 시간을 반환합니다.
