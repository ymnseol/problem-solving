# 프로그래머스 - 두 큐 합 같게 만들기(118667)
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    queue = queue1 + queue2
    left = 0
    right = len(queue) // 2 - 1
    curr_sum = sum(queue1)
    target = curr_sum + sum(queue2)
    if target % 2:
        return -1
    target //= 2
    cnt = 0
    while left <= right < len(queue):
        if curr_sum == target:
            return cnt
        elif curr_sum < target:
            right += 1
            if right < len(queue):
                curr_sum += queue[right]
            else:
                return -1
        else:
            curr_sum -= queue[left]
            left += 1
        cnt += 1
    return -1
