# 프로그래머스 - 신고 결과 받기(92334)
# https://school.programmers.co.kr/learn/courses/30/lessons/92334


def solution(id_list, report, k):
    reported = {id: set() for id in id_list}
    banned = {id: 0 for id in id_list}
    for r in report:
        r = r.split(" ")
        reported[r[1]].add(r[0])
    for r in reported.keys():
        if len(reported[r]) >= k:
            for n in reported[r]:
                banned[n] += 1
    return list(banned.values())
