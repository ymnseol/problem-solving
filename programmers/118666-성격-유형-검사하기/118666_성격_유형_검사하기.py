# 프로그래머스 - 성격 유형 검사하기(118666)
# https://school.programmers.co.kr/learn/courses/30/lessons/118666?

def solution(survey, choices):
    scores = dict()
    for c in ['RT', 'CF', 'JM', 'AN']:
        scores[c] = 0
    answer = ''
    for i in range(len(choices)):
        if survey[i][0] > survey[i][1]:
            survey[i] = survey[i][1] + survey[i][0]
            choices[i] = 8 - choices[i]
        scores[survey[i]] += choices[i] - 4
    for k, v in scores.items():
        if v <= 0:
            answer += k[0]
        else:
            answer += k[1]
    
    return answer
