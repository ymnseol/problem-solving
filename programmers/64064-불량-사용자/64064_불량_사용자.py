# 프로그래머스 - 불량 사용자(64064)
# https://school.programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import product

def solution(user_id, banned_id):
    banned_users = {bid.replace('*', '(\w|\d)') + str(i): set() for i, bid in enumerate(banned_id)}
    for uid in user_id:
        for bid in banned_users.keys():
            if re.fullmatch(bid[:-1], uid):
                banned_users[bid].add(uid)
    
    answer = set()
    for pair in product(*banned_users.values()):
        if frozenset(pair) not in answer and len(pair) == len(set(pair)):
            answer.add(frozenset(pair))
    return len(answer)
