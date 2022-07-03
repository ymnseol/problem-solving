# 더 맵게
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.</p>
<div class="highlight"><pre class="codehilite"><code>섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
</code></pre></div>
<p>Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.<br>
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>scoville의 길이는 2 이상 1,000,000 이하입니다.</li>
<li>K는 0 이상 1,000,000,000 이하입니다.</li>
<li>scoville의 원소는 각각 0 이상 1,000,000 이하입니다.</li>
<li>모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>scoville</th>
<th>K</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 9, 10, 12]</td>
<td>7</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<ol>
<li><p>스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.<br>
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5<br>
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]</p></li>
<li><p>스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.<br>
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13<br>
가진 음식의 스코빌 지수 = [13, 9, 10, 12]</p></li>
</ol>

<p>모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.</p>
</div>
    </div>

***
## 풀이
Min heap을 사용합니다.
```python
import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap) # min heapify
    
    cnt = 0

    if heap[0] >= K:
        return cnt
    
    while len(heap) > 1:
        cnt += 1
        first_min = heapq.heappop(heap)
        second_min = heapq.heappop(heap)
        
        new_scale = first_min + second_min * 2
        heapq.heappush(heap, new_scale)
        
        if heap[0] >= K:
            return cnt
    
    return -1
```
### 수행 과정
1. 주어진 스코빌 지수를 min heapify합니다.
2. 주어진 스코빌 지수 중 가장 작은 지수가 K 이상이라면, heap property에 따라 이미 모든 음식의 스코빌 지수가 K 이상입니다.  
   음식을 섞을 필요가 없습니다. 0을 반환합니다.
3. 가장 작은 지수가 K 미만이라면, 스코빌 지수가 K 미만인 음식이 적어도 1개 존재합니다.  
   조건을 만족할 때까지 음식을 섞습니다.  
   1. 가장 작은 스코빌 지수와 두번째로 가장 작은 스코빌 지수를 heap에서 꺼냅니다.
        > heapq의 heappop은 heap의 root를 꺼내더라도 heap property를 만족하도록 합니다.
   2. 섞은 스코빌 지수를 heap에 insert합니다.
        > heapq의 heappush는 heap에 새로운 item을 넣어도 heap property를 만족하도록 합니다.
   3. 만약 새로운 스코빌 지수가 추가된 heap의 가장 작은 지수가 K 이상이라면, heap property에 따라 이미 모든 음식의 스코빌 지수가 K 이상입니다.  
   더이상 음식을 섞을 필요가 없습니다. 섞은 횟수 cnt를 반환합니다.
4. 모든 음식을 섞어 남은 스코빌 지수는 1개입니다. 더이상 스코빌 지수를 증가시킬 수 없습니다.  
   남은 스코빌 지수가 K 미만이면 조건을 만족할 수 없습니다. -1을 반환합니다.
   
### 개선 과정
처음에는 아래와 같은 풀이를 제출하였습니다.
```python
import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap) # min heapify
    
    cnt = 0
    
    while len(heap) > 1:
        cnt += 1
        first_min = heapq.heappop(heap)
        second_min = heapq.heappop(heap)
        
        new_scale = first_min + second_min * 2
        heapq.heappush(heap, new_scale)
        
        if heap[0] >= K:
            return cnt
    
    return -1
```
위의 풀이는 프로그래머스에서 제공하는 모든 테스트 케이스와 효율성 테스트를 통과하여 정답 처리되었습니다.  
그러나 위의 풀이는 스코빌 지수가 1개 주어지고, 해당 스코빌 지수가 이미 K 이상일 때의 경우를 올바르게 처리하지 못합니다.  
예를 들어,  

| scoville | K | return |
|----------|---|--------|
| [7]      | 7 | 0      |  

의 경우, 위의 코드는 0 대신 -1을 반환합니다.
