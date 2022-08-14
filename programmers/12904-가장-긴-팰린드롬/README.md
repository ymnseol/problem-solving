# 가장 긴 팰린드롬

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.<br>
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.</p>

<p>예를들면, 문자열 s가 "abcdcba"이면 7을 return하고 "abacde"이면 3을 return합니다.</p>

<h5>제한사항</h5>

<ul>
<li>문자열 s의 길이 : 2,500 이하의 자연수</li>
<li>문자열 s는 알파벳 소문자로만 구성</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>"abcdcba"</td>
<td>7</td>
</tr>
<tr>
<td>"abacde"</td>
<td>3</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.</p>

<p>입출력 예 #2<br>
2번째자리 'b'를 기준으로 "aba"가 팰린드롬이 되므로 3을 return합니다.</p>
</div>
    </div>

***

## 풀이

Sliding window를 활용합니다.

```Python
def solution(s):
    for l in range(len(s) - 1, -1, -1):
        left, right = 0, l
        while right < len(s):
            if s[left:right + 1] != s[left:right+1][::-1]:
                left += 1
                right += 1
            else:
                return l + 1
```

### 수행 과정

1. 주어진 문자열의 총 길이를 시작으로 단위를 정해 문자열 일부를 탐색합니다.
2. 만약 해당 길이의 팰린드롬을 찾았다면, 그 팰린드롬이 주어진 문자열에서 찾을 수 있는 가장 긴 팰린드롬입니다. 길이를 반환합니다.
3. 만약 해당 길이의 팰린드롬을 찾지 못했다면, 탐색할 부분 문자열의 길이를 줄이고 위 과정을 반복합니다.

예를 들어, 'abcdcba'의 경우, 총 길이를 부분 문자열의 길이로 하여 탐색했을 때 가장 긴 팰린드롬을 찾을 수 있습니다.

![abcdcba](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_12904_1.png)

예를 들어, 'abacde'의 경우, 총 길이를 부분 문자열의 길이로 하여 탐색했을 때 팰린드롬을 찾을 수 없습니다.

![abacde-6](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_12904_2.png)

부분 문자열의 길이를 5로 줄여 탐색합니다. 팰린드롬을 찾을 수 없습니다.

![abacde-5](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_12904_3.png)

부분 문자열의 길이를 4로 줄여 탐색합니다. 팰린드롬을 찾을 수 없습니다.

![abacde-4](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_12904_4.png)

부분 문자열의 길이를 3으로 줄여 탐색합니다. 팰린드롬을 찾았습니다. 3을 반환하고 탐색을 종료합니다.

![abacde-3](https://github.com/ymnseol/problem-solving/blob/main/images/programmers_12904_5.png)
