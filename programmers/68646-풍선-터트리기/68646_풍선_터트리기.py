# 프로그래머스 - 풍선 터트리기(68646)
# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    cnt = 0
    left = [float('inf')] * len(a)
    left[0] = a[0]
    right = [float('inf')] * len(a)
    right[-1] = a[-1]
    for i in range(1, len(a)):
        left[i] = min(a[i], left[i - 1])
        right[len(a) - i - 1] = min(a[len(a) - i - 1], right[len(a) - i])
    for i, n in enumerate(a):
        if left[i] < n and right[i] < n:
            continue
        cnt += 1
            
    return cnt
