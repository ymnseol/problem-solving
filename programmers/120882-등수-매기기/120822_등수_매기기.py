# 프로그래머스 - 등수 매기기(120882)
# https://school.programmers.co.kr/learn/courses/30/lessons/120882


def solution(score):
    score = [e + m for e, m in score]
    sorted_score = sorted(score, reverse=True)
    return [sorted_score.index(s) + 1 for s in score]
