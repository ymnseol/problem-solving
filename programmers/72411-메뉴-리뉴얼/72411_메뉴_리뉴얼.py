# 프로그래머스 - 메뉴 리뉴얼(72411)
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    orders = [sorted(o) for o in orders]
    max_len = max(map(len, orders))
    course = [c for c in course if c <= max_len]
    
    sel = set()
    
    for c in course:
        comb = [''.join(co) for o in orders for co in combinations(o, c)]
        max_cnt = comb.count(max(comb, key=comb.count))
        if max_cnt >= 2:
            [sel.add(co) for co in comb if comb.count(co) == max_cnt]
    
    return sorted(list(sel))
