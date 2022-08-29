# 두 큐 합 같게 만들기

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 <strong>다른 큐</strong>에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다. 이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.</p>

<p>큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다. 즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다. 예를 들어 큐 <code>[1, 2, 3, 4]</code>가 주어졌을 때, pop을 하면 맨 앞에 있는 원소 1이 추출되어 <code>[2, 3, 4]</code>가 되며, 이어서 5를 insert하면 <code>[2, 3, 4, 5]</code>가 됩니다.</p>

<p>다음은 두 큐를 나타내는 예시입니다.</p>
<div class="highlight"><pre class="codehilite"><code>queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
</code></pre></div>
<p>두 큐에 담긴 모든 원소의 합은 30입니다. 따라서, 각 큐의 합을 15로 만들어야 합니다. 예를 들어, 다음과 같이 2가지 방법이 있습니다.</p>

<ol>
<li>queue2의 4, 6, 5를 순서대로 추출하여 queue1에 추가한 뒤, queue1의 3, 2, 7, 2를 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [4, 6, 5], queue2는 [1, 3, 2, 7, 2]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 7번 수행합니다.</li>
<li>queue1에서 3을 추출하여 queue2에 추가합니다. 그리고 queue2에서 4를 추출하여 queue1에 추가합니다. 그 결과 queue1은 [2, 7, 2, 4], queue2는 [6, 5, 1, 3]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 2번만 수행하며, 이보다 적은 횟수로 목표를 달성할 수 없습니다.</li>
</ol>

<p>따라서 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수는 2입니다.</p>

<p>길이가 같은 두 개의 큐를 나타내는 정수 배열 <code>queue1</code>, <code>queue2</code>가 매개변수로 주어집니다. 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>queue1</code>의 길이 = <code>queue2</code>의 길이 ≤ 300,000</li>
<li>1 ≤ <code>queue1</code>의 원소, <code>queue2</code>의 원소 ≤ 10<sup>9</sup></li>
<li>주의: 언어에 따라 합 계산 과정 중 산술 오버플로우 발생 가능성이 있으므로 long type 고려가 필요합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>queue1</th>
<th>queue2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[3, 2, 7, 2]</td>
<td>[4, 6, 5, 1]</td>
<td>2</td>
</tr>
<tr>
<td>[1, 2, 1, 2]</td>
<td>[1, 10, 1, 2]</td>
<td>7</td>
</tr>
<tr>
<td>[1, 1]</td>
<td>[1, 5]</td>
<td>-1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>두 큐에 담긴 모든 원소의 합은 20입니다. 따라서, 각 큐의 합을 10으로 만들어야 합니다. queue2에서 1, 10을 순서대로 추출하여 queue1에 추가하고, queue1에서 1, 2, 1, 2와 1(queue2으로부터 받은 원소)을 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [10], queue2는 [1, 2, 1, 2, 1, 2, 1]가 되며, 각 큐의 원소 합은 10으로 같습니다. 이때 작업 횟수는 7회이며, 이보다 적은 횟수로 목표를 달성하는 방법은 없습니다. 따라서 7를 return 합니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>어떤 방법을 쓰더라도 각 큐의 원소 합을 같게 만들 수 없습니다. 따라서 -1을 return 합니다.</p>
</div>
    </div>

---

## 풀이

Two pointers를 사용합니다.

```Python
from collections import deque

def solution(queue1, queue2):
    queue = queue1 + queue2
    left = 0
    right = len(queue) // 2 - 1
    curr_sum = sum(queue1)
    target = curr_sum + sum(queue2)
    if target % 2:
        return -1
    target //= 2
    cnt = 0
    while left <= right < len(queue):
        if curr_sum == target:
            return cnt
        elif curr_sum < target:
            right += 1
            if right < len(queue):
                curr_sum += queue[right]
            else:
                return -1
        else:
            curr_sum -= queue[left]
            left += 1
        cnt += 1
    return -1
```

### 수행 과정

1. 주어진 큐 두 개를 queue1, queue2 순서로 이어붙인 list를 만듭니다.
2. 포인터를 각각 queue1의 시작 위치, queue1의 끝 위치로 설정합니다.
3. 두 큐의 합이 같은지 확인하기 위해서는 큐 한 개의 합만 확인해도 충분합니다. queue1을 선택하여 현재 합을 정의합니다.
4. 만약 주어진 두 큐의 모든 원소의 합이 홀수일 경우, 두 큐의 합을 같게 만들 수 없습니다. -1을 반환합니다.
5. 주어진 두 큐의 모든 원소의 합이 짝수인 경우, 두 큐의 합을 같게 만들 수 있다고 기대할 수 있습니다. 목표 합을 주어진 모든 원소의 합의 절반으로 정의합니다.
6. queue1의 현재 합이 목표 합과 같을 경우, 현재까지의 포인터 이동횟수를 반환합니다.
7. queue1의 현재 합이 목표 합보다 작을 경우, queue2로부터 원소를 추가해야 합니다. queue1의 끝 위치를 가리키는 포인터를 1 증가시킵니다. 현재 합에 새로 가리키는 원소를 더합니다.
8. queue1의 현재 합이 목표 합보다 클 경우, queue1의 시작 위치 원소를 제거해야 합니다. queue1의 시작 위치를 가리키는 포인터를 1 증가시킵니다. 현재 합에 삭제된 원소를 뺍니다.
9. queue2의 모든 원소를 queue1으로 옮겼거나, queue1에 목표 합보다 큰 원소가 있는 경우 두 큐의 합을 같게 만들 수 없습니다. -1을 반환합니다.


### 개선 과정

처음에는 문제 그대로 두 큐를 이용해 enqueue와 dequeue를 반복했습니다.

```Python
from collections import deque

def solution(queue1, queue2):
    max_e = 0
    q1 = deque([])
    q2 = deque([])
    q1_sum = 0
    q2_sum = 0
    
    for i in range(max(len(queue1), len(queue2))):
        if i < len(queue1):
            e = queue1[i]
            q1.append(e)
            q1_sum += e
            if e > max_e:
                max_e = e
        if i < len(queue2):
            e = queue2[i]
            q2.append(e)
            q2_sum += e
            if e > max_e:
                max_e = e

    target = q1_sum + q2_sum
    if target % 2:
        return -1
    target //= 2
    
    if max_e > target:
        return -1
    
    cnt = 0
    
    while q1_sum != target:
        while q1_sum > target:
            e = q1.popleft()
            q1_sum -= e
            q2.append(e)
            q2_sum += e
            cnt += 1
        while q1_sum < target:
            e = q2.popleft()
            q2_sum -= e
            q1.append(e)
            q1_sum += e
            cnt += 1
    
    return cnt
```

합을 구하는 과정, 목표 합을 넘는 원소가 있는지 찾는 과정에서 소모하는 시간을 최대한 줄여 $\theta (n)$ 시간을 소모하도록 했고, deque를 사용해 popleft()가 $O(1)$ 시간만을 소모하게 했음에도 불구하고 시간 초과로 일부 테스트 케이스를 통과할 수 없었습니다.

두 큐를 사용하는 대신 시간을 줄이기 위해 큐의 FIFO 특성을 활용한 two pointers를 사용하였습니다.
