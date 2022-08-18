# N으로 표현

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.</p>

<p>12 = 5 + 5 + (5 / 5) + (5 / 5)<br>
12 = 55 / 5 + 5 / 5<br>
12 = (55 + 5) / 5</p>

<p>5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.<br>
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>N은 1 이상 9 이하입니다.</li>
<li>number는 1 이상 32,000 이하입니다.</li>
<li>수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.</li>
<li>최솟값이 8보다 크면 -1을 return 합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>N</th>
<th>number</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>2</td>
<td>11</td>
<td>3</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제 #1<br>
문제에 나온 예와 같습니다.</p>

<p>예제 #2<br>
<code>11 = 22 / 2</code>와 같이 2를 3번만 사용하여 표현할 수 있습니다.</p>

<p><a href="https://www.oi.edu.pl/old/php/show.php?ac=e181413&amp;module=show&amp;file=zadania/oi6/monocyfr" target="_blank" rel="noopener">출처</a></p>

<p>※ 공지 - 2020년 9월 3일 테스트케이스가 추가되었습니다.</p>
</div>
    </div>

***

## 풀이

동적계획법(Dynamic programming)을 사용합니다.

```Python
def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        num = int(str(N) * i)
        if num == number:
            return i
        dp[i].add(num)
        for j in range(1, i // 2 + 1):
            for n1 in dp[j]:
                for n2 in dp[i - j]:
                    if n1 + n2 == number:
                        return i
                    if n1 - n2 == number:
                        return i
                    if n2 - n1 == number:
                        return i
                    if n1 * n2 == number:
                        return i
                    if n2 and n1 // n2 == number:
                        return i
                    if n1 and n2 // n1 == number:
                        return i
                    
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n2 - n1)
                    dp[i].add(n1 * n2)
                    if n2:
                        dp[i].add(n1 // n2)
                    if n1:
                        dp[i].add(n2 // n1)
    
    return -1
```

### 수행 과정

1. 만약 주어진 N과 number가 같다면, N을 한 개만 사용해서 number를 만들 수 있습니다. 1을 반환합니다.
2. N은 최대 8개까지 사용할 수 있고, 8개를 사용해도 아직 number를 만들 수 없다면 8개를 초과하여 number를 만드는 과정을 수행할 필요가 없습니다. DP 테이블의 크기를 9로 고정합니다.
3. N을 i개 사용해서 만들 수 있는 수는 다음과 같습니다:
   
   1. N을 i개 이어붙인 수  
   예를 들어, N이 5일 때  
   i = 1: 1  
   i = 2: 11  
   i = 3: 111  
   ...
   2. N을 j개 사용해 만든 수와 N을 i-j개 사용해 만든 수를 사칙연산해 얻은 수  
   예를 들어, N이 5일 때  
   i = 2: N을 1개 사용해 만든 수와 N을 1개 사용해 만든 수를 사칙연산해 얻은 수  
   i = 3: N을 1개 사용해 만든 수와 N을 2개 사용해 만든 수를 사칙연산해 얻은 수  
   i = 4: N을 1개 사용해 만든 수와 N을 3개 사용해 만든 수를 사칙연산해 얻은 수, N을 2개 사용해 만든 수와 N을 2개 사용해 만든 수를 사칙연산해 얻은 수  
   i = 5: N을 1개 사용해 만든 수와 N을 4개 사용해 만든 수를 사칙연산해 얻은 수, N을 2개 사용해 만든 수와 N을 3개 사용해 만든 수를 사칙연산해 얻은 수  
   ...
   
   수를 만드는 과정에서 number와 같은 수가 만들어진 경우, i가 최소 N 사용횟수입니다. i를 반환합니다.
4. N을 8개 사용한 수를 모두 구했음에도 number를 만들 수 없다면 -1을 반환합니다.
