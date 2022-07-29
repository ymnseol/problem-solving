# 프로그래머스 - 땅따먹기(12913)
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for i in range(len(land) - 1, 0, -1):
        land[i - 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i - 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i - 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i - 1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[0])
