# 프로그래머스- - 튜플(64065)
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

import re

def solution(s):
    answer = []
    for p in sorted([list(r.split(',')) for r in re.findall(r'\d[,\d]*', s)], key=lambda x: len(x)):
        for n in p:
            if n not in answer:
                answer.append(n)
    return list(map(int, answer))
