# 프로그래머스 - [1차] 셔틀버스(17678)
# https://school.programmers.co.kr/learn/courses/30/lessons/17678

import string

def solution(n, t, m, timetable):
    START = 540
    hashtable = {START + t * i: [] for i in range(n)}
    crews = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    for crew in crews:
        for key in hashtable.keys():
            if crew <= key and len(hashtable[key]) < m:
                hashtable[key].append(crew)
                break
    last_key, last_value = list(hashtable.items())[-1]
    if len(last_value) < m:
        answer = last_key
    else:
        answer = last_value[-1] - 1
    return f'{str(answer // 60).zfill(2)}:{str(answer % 60).zfill(2)}'
