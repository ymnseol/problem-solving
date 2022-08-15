# 프로그래머스 - [카카오 인턴] 수식 최대화(67257)
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

import re
from itertools import permutations

def solution(expression):
    answer = 0
    priorities = permutations(set(re.findall(r'[-*+]', expression)))
    
    for priority in priorities:
        polynomial = re.findall(r'(\d+|[-*+]+)', expression)
        for operator in priority:
            i = 0
            while i < len(polynomial):
                if polynomial[i] == operator:
                    polynomial[i] = (str(eval(f'{polynomial[i - 1]}{polynomial[i]}{polynomial[i + 1]}')))
                    polynomial.pop(i - 1)
                    polynomial.pop(i)
                else:
                    i += 1
        answer = max(answer, abs(int(polynomial[0])))
    return answer
