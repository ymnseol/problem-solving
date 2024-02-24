# 프로그래머스 - 개인정보 수집 유효기간(150370)
# https://school.programmers.co.kr/learn/courses/30/lessons/150370


def str2timestamp(date_string):
    year, month, day = map(lambda x: int(x), date_string.split("."))
    return day + month * 28 + (year - 2000) * 28 * 12


def solution(today, terms, privacies):
    answer = []
    today = str2timestamp(today)
    terms = {term[0]: int(term[2:]) for term in terms}
    for i, privacy in enumerate(privacies):
        start_date, term = privacy.split()
        start_date = str2timestamp(start_date)
        if start_date + terms[term] * 28 <= today:
            answer.append(i + 1)
    return answer
