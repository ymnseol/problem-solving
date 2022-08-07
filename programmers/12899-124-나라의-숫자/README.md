# 124 나라의 숫자

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.</p>

<ol>
<li>124 나라에는 자연수만 존재합니다.</li>
<li>124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.</li>
</ol>

<p>예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.</p>
<table class="table">
        <thead><tr>
<th>10진법</th>
<th>124 나라</th>
<th>10진법</th>
<th>124 나라</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>6</td>
<td>14</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>7</td>
<td>21</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>8</td>
<td>22</td>
</tr>
<tr>
<td>4</td>
<td>11</td>
<td>9</td>
<td>24</td>
</tr>
<tr>
<td>5</td>
<td>12</td>
<td>10</td>
<td>41</td>
</tr>
</tbody>
      </table>
<p>자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.</p>

<h5>제한사항</h5>

<ul>
<li>n은 500,000,000이하의 자연수 입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td>4</td>
<td>11</td>
</tr>
</tbody>
      </table></div>
    </div>

***

## 풀이
```Python
def solution(n):
    digit = ['4', '1', '2']
    ans = ''
    while n:
        ans = digit[n % 3] + ans
        n = n // 3 - (not n % 3)
    return ans
```

### 수행 과정

124 나라의 숫자는 3진수와 유사하나 다른 점이 있습니다.  
일반적인 3진수에서 10(3)으로 넘어갈 때 124 나라에서는 자리수를 유지합니다.

| 10진수 | 3진수 | 124 나라의 숫자 |
|-------|------|--------------|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 10 | 4 |
| 4 | 11 | 11 |
| 5 | 12 | 12 |
| 6 | 20 | 14 |
| 7 | 21 | 21 |
| 8 | 22 | 22 |
| 9 | 100 | 24 |
| 10 | 101 | 41 |
| 11 | 102 | 42 |
| 12 | 110 | 44 |
| 13 | 111 | 111 |

3진수에서 자리수가 넘어가는 경우는 수가 10진수에서의 3의 배수일 때입니다.

1. 주어진 10진수의 일의 자리부터 124 나라의 숫자로 변환합니다. 124 나라의 숫자로 변환하기 위해 주어진 숫자를 3으로 나눴을 때의 나머지를 이용합니다.
2. 주어진 숫자를 3으로 나누어 다음 자리수를 계산할 수 있도록 합니다. 이때 숫자가 3의 배수일 경우 1을 빼주어 자리수를 맞춥니다.
