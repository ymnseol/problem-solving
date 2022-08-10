# 프로그래머스 - H-Index(42747)
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    return sum([1 for i in range(len(citations)) if citations[i] > i])
