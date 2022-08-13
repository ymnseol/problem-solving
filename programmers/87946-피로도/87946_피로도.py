# 프로그래머스 - 피로도(87946)
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    routes = permutations(dungeons, len(dungeons))
    max_dungeons = 0
    for r in routes:
        if max_dungeons == len(dungeons):
            break
        tmp = k
        cnt = 0
        for d in r:
            if tmp >= d[0]:
                tmp -= d[1]
                cnt += 1
            else:
                break
        max_dungeons = max(max_dungeons, cnt)
    return max_dungeons
