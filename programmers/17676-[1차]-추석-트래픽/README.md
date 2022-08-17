# [1차] 추석 트래픽

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><h2>추석 트래픽</h2>

<p>이번 추석에도 시스템 장애가 없는 명절을 보내고 싶은 어피치는 서버를 증설해야 할지 고민이다. 장애 대비용 서버 증설 여부를 결정하기 위해 작년 추석 기간인 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량을 계산해보기로 했다. <strong>초당 최대 처리량</strong>은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다. </p>

<h3>입력 형식</h3>

<ul>
<li><code>solution</code> 함수에 전달되는 <code>lines</code> 배열은 <strong>N</strong>(1 ≦ <strong>N</strong> ≦ 2,000)개의 로그 문자열로 되어 있으며,
각 로그 문자열마다 요청에 대한 응답완료시간 <strong>S</strong>와 처리시간 <strong>T</strong>가 공백으로 구분되어 있다.</li>
<li>응답완료시간 <strong>S</strong>는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 <code>2016-09-15 hh:mm:ss.sss</code> 형식으로 되어 있다.</li>
<li>처리시간 <strong>T</strong>는 <code>0.1s</code>, <code>0.312s</code>, <code>2s</code> 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 <code>s</code>로 끝난다.</li>
<li>예를 들어, 로그 문자열 <code>2016-09-15 03:10:33.020 0.011s</code>은 "2016년 9월 15일 오전 3시 10분 <strong>33.010초</strong>"부터 "2016년 9월 15일 오전 3시 10분 <strong>33.020초</strong>"까지 "<strong>0.011초</strong>" 동안 처리된 요청을 의미한다. <strong>(처리시간은 시작시간과 끝시간을 포함)</strong></li>
<li>서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 <strong>0.001 ≦ T ≦ 3.000</strong>이다.</li>
<li><code>lines</code> 배열은 응답완료시간 <strong>S</strong>를 기준으로 오름차순 정렬되어 있다.</li>
</ul>

<h3>출력 형식</h3>

<ul>
<li><code>solution</code> 함수에서는 로그 데이터 <code>lines</code> 배열에 대해 <strong>초당 최대 처리량</strong>을 리턴한다.</li>
</ul>

<h3>입출력 예제</h3>

<h4>예제1</h4>

<ul>
<li><p>입력: [<br>
"2016-09-15 01:00:04.001 2.0s",<br>
"2016-09-15 01:00:07.000 2s"<br>
]</p></li>
<li><p>출력: 1</p></li>
</ul>

<h4>예제2</h4>

<ul>
<li><p>입력: [<br>
"2016-09-15 01:00:04.002 2.0s",<br>
"2016-09-15 01:00:07.000 2s"<br>
]</p></li>
<li><p>출력: 2</p></li>
<li><p>설명: 처리시간은 시작시간과 끝시간을 <strong>포함</strong>하므로 <br>
첫 번째 로그는 <code>01:00:02.003 ~ 01:00:04.002</code>에서 2초 동안 처리되었으며,<br>
두 번째 로그는 <code>01:00:05.001 ~ 01:00:07.000</code>에서 2초 동안 처리된다.<br>
따라서, 첫 번째 로그가 끝나는 시점과 두 번째 로그가 시작하는 시점의 구간인 <code>01:00:04.002 ~ 01:00:05.001</code> 1초 동안 최대 2개가 된다.</p></li>
</ul>

<h4>예제3</h4>

<ul>
<li><p>입력: [<br>
"2016-09-15 20:59:57.421 0.351s",<br>
"2016-09-15 20:59:58.233 1.181s",<br>
"2016-09-15 20:59:58.299 0.8s",<br>
"2016-09-15 20:59:58.688 1.041s",<br>
"2016-09-15 20:59:59.591 1.412s",<br>
"2016-09-15 21:00:00.464 1.466s",<br>
"2016-09-15 21:00:00.741 1.581s",<br>
"2016-09-15 21:00:00.748 2.31s",<br>
"2016-09-15 21:00:00.966 0.381s",<br>
"2016-09-15 21:00:02.066 2.62s"<br>
]</p></li>
<li><p>출력: 7</p></li>
<li><p>설명: 아래 타임라인 그림에서 빨간색으로 표시된 1초 각 구간의 처리량을 구해보면 <code>(1)</code>은 4개, <code>(2)</code>는 7개, <code>(3)</code>는 2개임을 알 수 있다. 따라서 <strong>초당 최대 처리량</strong>은 7이 되며, 동일한 최대 처리량을 갖는 1초 구간은 여러 개 존재할 수 있으므로 이 문제에서는 구간이 아닌 개수만 출력한다.<br>
<img src="http://t1.kakaocdn.net/welcome2018/chuseok-01-v5.png" title="" alt="Timeline"></p></li>
</ul>

<p><a href="http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/" target="_blank" rel="noopener">해설 보러가기</a></p>
</div>
    </div>

***

## 풀이

Min heap과 Two pointers를 활용합니다.

```Python
import heapq

def solution(lines):
    max_cnt = 0
    times = []
    
    for i in range(len(lines)):
        finish = int(lines[i][11:13]) * 3600 + int(lines[i][14:16]) * 60 + float(lines[i][17:23])
        start = finish - float(lines[i][24:-1]) +  0.001
        finish, start = round(finish, 3), round(start, 3)
        lines[i] = (start, finish)
        times.append(start)
        times.append(finish)
    
    times.sort()
    lines.sort()
    curr = 0
    curr_jobs = []
    
    for time in times:
        while curr_jobs and curr_jobs[0][0] < time:
            heapq.heappop(curr_jobs)
        while curr < len(lines) and lines[curr][0] <= round(time + 0.999, 3):
            heapq.heappush(curr_jobs, (lines[curr][1], lines[curr][0]))
            curr += 1
        max_cnt = max(max_cnt, len(curr_jobs))
        
    return max_cnt
```

### 수행 과정

1. 각 로그 데이터의 처리 시작시각과 완료시각을 구합니다. 로그 데이터를 (시작시각, 완료시각) 쌍으로 대체하고, 시작시각과 완료시각을 times에 삽입합니다.
2. 시작시각과 완료시각이 모두 저장된 times를 오름차순 정렬합니다. 이 시각 목록은 처리되는 요청의 개수가 변화할 수 있는 시점들과 같습니다.
3. 완료시각을 기준으로 정렬되어 있던 lines를 시작시각을 기준으로 정렬합니다.
4. times의 변화 가능 시점 time을 기준으로, 새롭게 정의된 1초 구간은 [time, time + 0.999]입니다. 이전에 처리되고 있는 요청 목록 중 완료시각이 time보다 작은 요청은 이제 이 구간 내에서 처리되는 요청이 아닙니다. 목록에서 제거합니다.
5. 아직 처리되고 있지 않은 요청 중 시작시각이 time + 0.999보다 작거나 같은 경우, 처리되고 있는 요청 목록에 추가합니다.
6. 처리되고 있는 요청의 개수가 지금까지 구한 최대 개수보다 큰 경우, 값을 갱신합니다.
7. 모든 시점에 대해 처리되고 있는 요청의 개수를 확인할 때까지 위 작업을 반복합니다.
