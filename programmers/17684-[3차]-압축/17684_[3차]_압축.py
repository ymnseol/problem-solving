# 프로그래머스 - [3차] 압축(17684)
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    
    indices = dict()
    for i, c in enumerate(map(chr, range(ord('A'), ord('Z') + 1))):
        indices[c] = i + 1
    
    left = 0
    right = 1
    
    while right <= len(msg) and left <= right:
        submsg = msg[left:right]
        if not indices.get(submsg):
            print('not in dict')
            answer.append(indices[submsg[:-1]])
            indices[submsg] = len(indices) + 1
            left = right - 1
        right += 1
    answer.append(indices[msg[left:right]])
    return answer
