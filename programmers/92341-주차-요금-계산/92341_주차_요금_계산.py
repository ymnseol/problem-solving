# 프로그래머스 - 주차 요금 계산(92341)
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil
from collections import defaultdict

def additional_fee(fee_table, time):
    additional_time = ceil((time - fee_table[0]) / fee_table[2])
    return additional_time * fee_table[3] if additional_time > 0 else 0

def solution(fees, records):
    timestamps = defaultdict(list)
    time = defaultdict(lambda: 0)
    fee = defaultdict(lambda: fees[1])
    
    for record in records:
        timestamps[record[6:10]].append(int(record[:2]) * 60 + int(record[3:5]))
    
    for car, timestamp in timestamps.items():
        if len(timestamp) % 2:
            timestamp.append(1439)
        for i in range(0, len(timestamp) - 1, 2):
            time[car] += timestamp[i + 1] - timestamp[i]
        fee[car] += additional_fee(fees, time[car])
    
    return [fee[car] for car in sorted(fee.keys())]
