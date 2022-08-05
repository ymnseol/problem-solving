# 멀쩡한 사각형
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>가로 길이가 Wcm, 세로 길이가 Hcm인 직사각형 종이가 있습니다. 종이에는 가로, 세로 방향과 평행하게 격자 형태로 선이 그어져 있으며, 모든 격자칸은 1cm x 1cm 크기입니다. 이 종이를 격자 선을 따라 1cm × 1cm의 정사각형으로 잘라 사용할 예정이었는데, 누군가가 이 종이를 대각선 꼭지점 2개를 잇는 방향으로 잘라 놓았습니다. 그러므로 현재 직사각형 종이는 크기가 같은 직각삼각형 2개로 나누어진 상태입니다. 새로운 종이를 구할 수 없는 상태이기 때문에, 이 종이에서 원래 종이의 가로, 세로 방향과 평행하게 1cm × 1cm로 잘라 사용할 수 있는 만큼만 사용하기로 하였습니다. <br>
가로의 길이 W와 세로의 길이 H가 주어질 때, 사용할 수 있는 정사각형의 개수를 구하는 solution 함수를 완성해 주세요.</p>

<h5>제한사항</h5>

<ul>
<li>W, H : 1억 이하의 자연수</li>
</ul>

<h4>입출력 예</h4>
<table class="table">
        <thead><tr>
<th>W</th>
<th>H</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>8</td>
<td>12</td>
<td>80</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
가로가 8, 세로가 12인 직사각형을 대각선 방향으로 자르면 총 16개 정사각형을 사용할 수 없게 됩니다. 원래 직사각형에서는 96개의 정사각형을 만들 수 있었으므로, 96 - 16 = 80 을 반환합니다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/ee895b2cd9/567420db-20f4-4064-afc3-af54c4a46016.png" title="" alt="572957326.92.png"></p>
</div>
    </div>

***

## 풀이

```Python
def solution(w, h):
    a, b = max(w, h), min(w, h)
    while b > 0:
        r = a % b
        a = b
        b = r
    return w * h - (w + h - a)
```

### 수행 과정
주어진 두 변의 최대공약수를 구합니다. 구한 최대공약수는 문제를 쪼개는 데에 사용됩니다.

예를 들어, 가로가 8, 세로가 12인 직사각형이 아래와 같이 주어질 때,

![split](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_62048_2.png)

두 변의 최대공약수인 4로 각 변을 나누어 가로가 2, 세로가 3인 직사각형으로 나눌 수 있습니다. 이때, 쪼개진 직사각형은 주어진 가로 변인 8을 쪼개진 직사각형의 가로 변인 2로 나눈 수인 4개 입니다. (쪼개진 직사각형의 개수는 세로 변을 이용해도 같습니다.)

쪼개진 직사각형 한 개를 봤을 때, 직사각형 내에서 사용할 수 없게 되는 정사각형의 개수는 쪼개진 직사각형의 가로 변과 세로 변을 합친 것에 중복된 1개를 빼주는 것과 같습니다.

전체 직사각형을 보았을 때, 사용할 수 없는 정사각형의 개수는 직사각형의 가로 변과 세로 변을 더하고 두 변의 최대공약수를 뺀 값과 같습니다.

### 개선 과정

```Python
def solution(w, h):
    w, h = max(w, h), min(w, h)
    a, b = w, h
    while b > 0:
        r = a % b
        a = b
        b = r
    nw, nh = w / a, h / a
    rt = w / (w / a)
    return w * h - rt * (nw + nh - 1)
```

위의 수행 과정을 따라 코드를 작성하고, 최종 풀이와 같이 식을 정리했습니다.