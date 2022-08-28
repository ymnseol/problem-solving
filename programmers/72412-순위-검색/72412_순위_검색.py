# 프로그래머스 - 순위 검색(72412)
# https://school.programmers.co.kr/learn/courses/30/lessons/72412#

from bisect import bisect_left, insort
from itertools import combinations

def solution(info, query):
    answer = []
    
    classification = dict()
    indices_for_wildcard = range(0, 4)
    
    for i in range(len(info)):
        props = info[i].split()
        score = int(props.pop())
        for n_wildcards in range(5):
            for com in map(set, combinations(indices_for_wildcard, n_wildcards)):
                q = ' '.join(['-' if j in com else props[j] for j in range(len(props))])
                if classification.get(q):
                    insort(classification[q], score)
                else:
                    classification[q] = [score]
    
    for q in query:
        props = q.replace('and ', '').split()
        score_limit = int(props.pop())
        props = ' '.join(props)
        if classification.get(props):
            answer.append(len(classification[props]) - bisect_left(classification[props], score_limit))
        else:
            answer.append(0)
    
    return answer
