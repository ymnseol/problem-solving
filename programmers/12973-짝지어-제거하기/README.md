# 짝지어 제거하기
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.</p>

<p>예를 들어, 문자열 S = <code>baabaa</code> 라면</p>

<p>b <em>aa</em> baa → <em>bb</em> aa → <em>aa</em> →</p>

<p>의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.</p>

<h5>제한사항</h5>

<ul>
<li>문자열의 길이 : 1,000,000이하의 자연수</li>
<li>문자열은 모두 소문자로 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>baabaa</td>
<td>1</td>
</tr>
<tr>
<td>cdcd</td>
<td>0</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
위의 예시와 같습니다.<br>
입출력 예 #2<br>
문자열이 남아있지만 짝지어 제거할 수 있는 문자열이 더 이상 존재하지 않기 때문에 0을 반환합니다.</p>

<p>※ 공지 - 2020년 6월 8일 테스트케이스가 추가되었습니다.</p>
</div>
    </div>

***

## 풀이
Stack을 사용합니다.
```Python
def solution(s):
    if len(s) % 2 == 1: return 0
    
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return 0 if stack else 1
```
### 수행 과정
1. 문자열의 길이가 홀수이면, 절대 모든 글자를 제거할 수 없습니다. 0을 반환합니다.
2. 문자열의 길이가 짝수이면, 주어진 문자열의 모든 글자에 대해 다음과 같은 작업을 수행합니다:
   1. 만약 stack이 비어 있지 않고, stack의 top element가 현재 글자와 같다면 stack에서 top element를 꺼냅니다.
   2. stack이 비어있거나 stack의 top element가 현재 글자와 같지 않다면, 글자를 짝지을 수 없습니다. 해당 글자를 stack에 push합니다.
3. stack이 비어있다면, 모든 글자가 짝지어 제거되었습니다. 1을 반환합니다.  
   stack이 비어있지 않다면, 모든 글자를 제거하지 못하였습니다. 0을 반환합니다.
