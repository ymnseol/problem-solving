# 프로그래머스 - 표현 가능한 이진트리(150367)
# https://school.programmers.co.kr/learn/courses/30/lessons/150367

from math import log2

def search(start, end, parent, tree):
    mid = (start + end) // 2
    curr = tree[mid]
    if parent == "0" and curr == "1":
        return False
    if start == end:
        return True
    left = search(start, mid - 1, curr, tree)
    right = search(mid + 1, end, curr, tree)
    if left and right:
        return True
    else:
        return False

def solution(numbers):
    answer = []
    for n in numbers:
        b = bin(n)[2:]
        b = b.zfill(2 ** (int(log2(len(b))) + 1) - 1)
        if search(0, len(b) - 1, b[len(b) // 2], b):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer   
