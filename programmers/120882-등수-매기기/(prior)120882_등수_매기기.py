# 프로그래머스 - 등수 매기기(120882)
# https://school.programmers.co.kr/learn/courses/30/lessons/120882


def solution(score):
    answer = [0] * len(score)
    score_sum = sorted(
        [(i, eng_score + mat_score) for i, (eng_score, mat_score) in enumerate(score)],
        key=lambda item: item[1],
        reverse=True,
    )
    current_rank = 1
    current_stack = 0
    current_score = -1
    for score_id, score in score_sum:
        if score == current_score:
            current_stack += 1
            answer[score_id] = current_rank
        else:
            current_rank += current_stack
            answer[score_id] = current_rank
            current_stack = 1
        current_score = score
    return answer
