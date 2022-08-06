# 프로그래머스 - 디스크 컨트롤러(42627)
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    visited = set()
    jobs.sort()
    pq = [[jobs[0][1], jobs[0][0]]]
    curr_time = jobs[0][0]
    total_time = 0
    
    while pq:
        required_time, start_time = heapq.heappop(pq)
        visited.add((start_time, required_time))
        total_time += curr_time + required_time - start_time
        if len(visited) < len(jobs):
            curr_time = max(curr_time + required_time, jobs[len(visited)][0])
        else:
            curr_time += required_time
        pq = [[r, s] for s, r in jobs if s <= curr_time and (s, r) not in visited]
        heapq.heapify(pq)
    return total_time // len(jobs)
