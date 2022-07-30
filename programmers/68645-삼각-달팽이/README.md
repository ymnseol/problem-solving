# 삼각 달팽이

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e1e53b93-dcdf-446f-b47f-e8ec1292a5e0/examples.png" title="" alt="examples.png"></p>

<hr>

<h5>제한사항</h5>

<ul>
<li>n은 1 이상 1,000 이하입니다.</li>
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
<td>4</td>
<td><code>[1,2,9,3,10,8,4,5,6,7]</code></td>
</tr>
<tr>
<td>5</td>
<td><code>[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]</code></td>
</tr>
<tr>
<td>6</td>
<td><code>[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]</code></td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>
</div>
    </div>

***

## 풀이

```Python
def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    dr = [1, 0, -1] # 0: top to down, 1: left to right, 2: down to top
    dc = [0, 1, -1]
    turn = r = c = 0
    num = 1
    
    for limit in range(n):
        for _ in range(n - limit):
            answer[r][c] = num
            num += 1
            r += dr[turn]
            c += dc[turn]
        r -= dr[turn]
        c -= dc[turn]
        turn = (turn + 1) % 3
        r += dr[turn]
        c += dc[turn]

    return sum(answer, []) # flatten

```

### 수행 과정

1. 아래 그림과 같은 2차원 List를 선언합니다. 이는 삼각형을 왼쪽 정렬한 형태와 같습니다.
   
   ![2-dimension list with zeros](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_68645_1.png)

2. 각 행의 0번째 열의 값을 update합니다. n개의 값이 update됩니다. 이 과정은 삼각형의 제일 위 꼭짓점부터 왼쪽 변을 따라 왼쪽 아래 꼭짓점까지 달팽이 채우기를 진행하는 과정과 같습니다.
   
   ![List: first update](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_68645_2.png)

3. 가장 마지막 행의 값을 update합니다. 이미 전 단계에서 0번째 열의 값을 update했기 때문에, 1번째 열부터 마지막 열까지의 값을 update합니다. n-1개의 값이 update됩니다. 이 과정은 삼각형의 왼쪽 아래 꼭짓점부터 아래의 변을 따라 오른쪽 아래 꼭짓점까지 달팽이 채우기를 진행하는 과정과 같습니다.
   
   ![List: second update](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_68645_3.png)

4. 각 행의 마지막 열의 값을 update합니다. 이미 전 단계에서 마지막 행과 0번째 행의 마지막 열의 값을 update했기 때문에, 해당 두 행을 제외한 나머지 행의 마지막 열의 값을 update합니다. n-2개의 값이 update됩니다. 이 과정은 삼각형의 오른쪽 아래 꼭짓점부터 오른쪽 변을 따라 제일 위의 꼭짓점까지 달팽이 채우기를 진행하는 과정과 같습니다.
   
   ![List: third update](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_68645_4.png)

5. 위의 과정을 반복합니다.
   
   ![List: last update](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_68645_5.png)

### 개선 과정

1. 방향에 맞게 숫자를 assign합니다.
2. 방향을 틀어야 할 때, 방향을 틉니다.

이 때 방향을 틀어야 할 때를 어떻게 알 수 있을지 고민했습니다.

처음에는 특정 방향으로 진행 중 index가 주어진 list의 index 범위를 벗어나거나, 방향에 따라 다음으로 assign할 자리에 이미 assign이 된 적이 있는 경우 방향을 틀도록 코드를 작성하고자 했습니다.

그런데 '다음으로 assign할 자리에 이미 assign이 된 적이 있는 경우'를 판별할 좋은 구현 방법이 떠오르지 않았습니다.

이를 보완할 수 있는 추가적인 규칙성으로, 한 방향으로 진행할 때 assign되는 숫자의 개수가 n개에서 방향을 틀 때마다 1개씩 줄어든다는 것을 채택하였습니다.

```Python
def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    r = c = 0
    num = 1
    
    for limit in range(n):
        if limit % 3 == 0:
            for _ in range(n - limit):
                answer[r][c] = num
                num += 1
                r += 1
            r -= 1
            c += 1
        elif limit % 3 == 1:
            for _ in range(n - limit):
                answer[r][c] = num
                num += 1
                c += 1
            r -= 1
            c -= 2
        elif limit % 3 == 2:
            for _ in range(n - limit):
                answer[r][c] = num
                num += 1
                r -= 1
                c -= 1
            r += 2
            c += 1
    
    return sum(answer, [])
```
위의 풀이는 모든 테스트 케이스를 통과하여 정답 처리되었습니다.

그러나 통과를 우선으로 하여 작성한 코드였기에 가독성이 좋지 않았습니다.  
방향 당 assign되는 숫자의 개수가 정해져 있음에도 IndexError를 방지하기 위해 'c -= 2' 등의 후처리가 필요해 지저분했습니다.

진행 방향은 세 가지로 정해져 있기 때문에, list를 사용하여 미리 진행 방향을 선언하여 가독성을 높이고자 하였습니다.

```Python
def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    dr = [1, 0, -1] # 0: top to down, 1: left to right, 2: down to top
    dc = [0, 1, -1]
    turn = r = c = 0
    num = 1
    
    for limit in range(n):
        for _ in range(n - limit):
            answer[r][c] = num
            num += 1
            r += dr[turn]
            c += dc[turn]
        r -= dr[turn]
        c -= dc[turn]
        turn = (turn + 1) % 3
        r += dr[turn]
        c += dc[turn]

    return sum(answer, []) # flatten
```
