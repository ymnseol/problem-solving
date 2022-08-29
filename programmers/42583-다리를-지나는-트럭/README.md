# 다리를 지나는 트럭

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.</p>

<p>예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.</p>
<table class="table">
        <thead><tr>
<th>경과 시간</th>
<th>다리를 지난 트럭</th>
<th>다리를 건너는 트럭</th>
<th>대기 트럭</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>[]</td>
<td>[]</td>
<td>[7,4,5,6]</td>
</tr>
<tr>
<td>1~2</td>
<td>[]</td>
<td>[7]</td>
<td>[4,5,6]</td>
</tr>
<tr>
<td>3</td>
<td>[7]</td>
<td>[4]</td>
<td>[5,6]</td>
</tr>
<tr>
<td>4</td>
<td>[7]</td>
<td>[4,5]</td>
<td>[6]</td>
</tr>
<tr>
<td>5</td>
<td>[7,4]</td>
<td>[5]</td>
<td>[6]</td>
</tr>
<tr>
<td>6~7</td>
<td>[7,4,5]</td>
<td>[6]</td>
<td>[]</td>
</tr>
<tr>
<td>8</td>
<td>[7,4,5,6]</td>
<td>[]</td>
<td>[]</td>
</tr>
</tbody>
      </table>
<p>따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.</p>

<p>solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 조건</h5>

<ul>
<li>bridge_length는 1 이상 10,000 이하입니다.</li>
<li>weight는 1 이상 10,000 이하입니다.</li>
<li>truck_weights의 길이는 1 이상 10,000 이하입니다.</li>
<li>모든 트럭의 무게는 1 이상 weight 이하입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bridge_length</th>
<th>weight</th>
<th>truck_weights</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>2</td>
<td>10</td>
<td>[7,4,5,6]</td>
<td>8</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>[10]</td>
<td>101</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>[10,10,10,10,10,10,10,10,10,10]</td>
<td>110</td>
</tr>
</tbody>
      </table>
<p><a href="http://icpckorea.org/2016/ONLINE/problem.pdf" target="_blank" rel="noopener">출처</a></p>

<p>※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.</p>
</div>
    </div>

---

## 풀이

queue를 사용합니다.

```Python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length - 1)])
    sum_on_bridge = 0
    n_trucks_on_bridge = 0
    
    while bridge:
        time += 1
        
        truck_passed = bridge.popleft()
        if truck_passed:
            sum_on_bridge -= truck_passed
            n_trucks_on_bridge -= 1
        
        if n_trucks_on_bridge == bridge_length:
            continue
        
        if truck_weights and sum_on_bridge + truck_weights[0] <= weight:
            truck_entering = truck_weights.popleft()
            sum_on_bridge += truck_entering
            n_trucks_on_bridge += 1
            for _ in range(0, bridge_length - len(bridge) - 1):
                bridge.append(0)
            bridge.append(truck_entering)
    
    return time
```

## 수행 과정

1. bridge는 다리 위 트럭 상황을 표현하기 위한 큐입니다.
2. 다리 위의 트럭은 1초에 1만큼의 거리를 이동합니다. 다리에서 현재 트럭이 위치하는 부분을 알기 위해 초기에 (다리 길이 - 1)만큼의 0을 삽입합니다. 나머지 한 자리는 처음으로 다리에 올라갈 트럭을 위한 자리입니다.
3. 모든 트럭이 다리를 건너 다리에 아무 트럭도 없을 때까지 다음과 같은 작업을 수행합니다:
   1. 소요시간을 1 증가시킵니다.
   2. bridge에서 dequeue를 수행합니다. 만약 dequeue된 값이 0이라면, 다리를 건넌 트럭은 없고, 다리 위 트럭이 1만큼 움직인 것을 의미합니다.
   3. dequeue된 값이 0이 아니라면, 이는 방금 하나의 트럭이 다리를 완전히 건넌 것을 의미합니다. 다리 위에 있는 트럭들의 무게 합에서 방금 다리를 빠져나온 트럭의 무게를 뺍니다. 다리 위에 있는 트럭의 수를 1 줄입니다.
   4. 만약 다리의 모든 구간에 빠짐 없이 트럭이 위치한다면, 최소한 다리 위의 트럭 한 대가 빠져나가야 합니다. 트럭을 새로 다리 위에 올리지 않습니다.
   5. 만약 다리 위에 자리가 있고, 아직 다리에 진입하지 못한 트럭이 존재하며, 트럭을 다리 위에 올려도 무게 제한을 초과하지 않는다면 다리에 트럭을 올립니다. 이때 해당 트럭이 이동하는 거리를 나타내기 위해, bridge에 (총 다리 길이 - 다리 위의 가장 마지막 트럭의 위치 - 1)만큼의 0을 enqueue합니다. 이후 트럭을 bridge에 enqueue합니다.
4. 소요시간을 반환합니다.
