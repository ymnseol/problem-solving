# 프로그래머스 - [1차] 다트 게임(17682)
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

import re


def solution(dartResult):
    areas = {"S": lambda x: x, "D": lambda x: x**2, "T": lambda x: x**3}
    options = {"*": ((lambda x: x * 2), True), "#": ((lambda x: -x), False)}

    dartTries = [
        re.findall(r"[0-9]+|[DST]|[#*]", dartTry)
        for dartTry in re.findall(r"[0-9]+[DST][#*]*", dartResult)
    ]

    scores = []
    for dartTry in dartTries:
        score, bonus = int(dartTry[0]), areas[dartTry[1]]
        option, applyToPrevScore = (
            options[dartTry[2]] if len(dartTry) == 3 else (None, False)
        )
        if not scores:
            applyToPrevScore = False
        current_score = bonus(score)
        if option:
            current_score = option(current_score)
            if applyToPrevScore:
                scores[-1] = option(scores[-1])
        scores.append(current_score)
    return sum(scores)
