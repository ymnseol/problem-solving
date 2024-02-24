# 프로그래머스 - 성격 유형 검사하기(118666)
# https://programmers.co.kr/learn/courses/30/lessons/118666


def solution(survey, choices):
    scores = {type_pair: 0 for type_pair in ["RT", "CF", "JM", "AN"]}
    for type_pair, choice in zip(survey, choices):
        if type_pair[0] > type_pair[1]:
            type_pair = type_pair[::-1]
            choice = 8 - choice
        scores[type_pair] += choice - 4
    return "".join(
        [
            type_pair[1] if score > 0 else type_pair[0]
            for type_pair, score in scores.items()
        ]
    )
