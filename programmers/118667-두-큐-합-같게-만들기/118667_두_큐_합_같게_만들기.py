# 프로그래머스 - 두 큐 합 같게 만들기(118667)
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    max_e = 0
    q1 = deque([])
    q2 = deque([])
    q1_sum = 0
    q2_sum = 0
    
    for i in range(max(len(queue1), len(queue2))):
        if i < len(queue1):
            e = queue1[i]
            q1.append(e)
            q1_sum += e
            if e > max_e:
                max_e = e
        if i < len(queue2):
            e = queue2[i]
            q2.append(e)
            q2_sum += e
            if e > max_e:
                max_e = e

    target = q1_sum + q2_sum
    if target % 2:
        return -1
    target //= 2
    
    if max_e > target:
        return -1
    
    cnt = 0
    
    while q1_sum != target:
        while q1_sum > target:
            e = q1.popleft()
            q1_sum -= e
            q2.append(e)
            q2_sum += e
            cnt += 1
        while q1_sum < target:
            e = q2.popleft()
            q2_sum -= e
            q1.append(e)
            q1_sum += e
            cnt += 1
    
    return cnt
