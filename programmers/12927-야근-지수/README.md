# 야근 지수

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,  퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li><code>works</code>는 길이 1 이상, 20,000 이하인 배열입니다.</li>
<li><code>works</code>의 원소는 50000 이하인 자연수입니다.</li>
<li><code>n</code>은 1,000,000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>works</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[4, 3, 3]</td>
<td>4</td>
<td>12</td>
</tr>
<tr>
<td>[2, 1, 2]</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td>[1,1]</td>
<td>3</td>
<td>0</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
n=4 일 때, 남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 4시간동안 일을 한 결과는 [2, 2, 2]입니다. 이 때 야근 지수는 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 12 입니다.</p>

<p>입출력 예 #2<br>
n=1일 때, 남은 일의 작업량이 [2,1,2]라면 야근 지수를 최소화하기 위해 1시간동안 일을 한 결과는 [1,1,2]입니다. 야근지수는 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> = 6입니다.</p>

<p>입출력 예 #3</p>

<p>남은 작업량이 없으므로 피로도는 0입니다.</p>
</div>
    </div>

***

## 풀이

최대 힙(Max heap)을 사용합니다.

```Python
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    max_pq = [-w for w in works]
    heapq.heapify(max_pq)
    for _ in range(n):
        top = heapq.heappop(max_pq)
        top += 1
        heapq.heappush(max_pq, top)
    return sum([n ** 2 for n in max_pq])
```

### 수행 과정

제곱을 사용하는 야근 지수가 최소가 되기 위해서는, 작업량이 적은 작업을 먼저 완료하는 것보다 작업량이 많은 작업을 수행해 제곱근의 크기를 줄이는 것이 중요합니다.

1. 만약 주어진 시간 내에 모든 작업을 완료할 수 있으면, 야근을 할 필요가 없습니다. 0을 반환합니다.
2. 작업량이 가장 많이 남은 작업을 찾습니다. 해당 작업을 한 번 처리합니다. 작업량이 1 작아집니다. 작업량을 갱신합니다.
3. 주어진 시간이 다 될 때까지 위의 작업을 반복합니다.
4. 주어진 시간 동안 할 수 있는 만큼 일을 수행했습니다. 각 남은 작업량의 제곱을 더한 값인 최소 야근 피로도를 반환합니다.
