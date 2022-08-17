# 프로그래머스 - 추석 트래픽(17676)
# https://school.programmers.co.kr/learn/courses/30/lessons/17676

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
