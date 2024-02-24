# 프로그래머스 - 개인정보 수집 유효기간(150370)
# https://school.programmers.co.kr/learn/courses/30/lessons/150370


def convert_to_timestamp(date_string):
    year, month, day = map(int, date_string.split("."))
    return day + month * 28 + (year - 2000) * 28 * 12


def solution(today, terms, privacies):
    today = convert_to_timestamp(today)
    terms = {term[0]: int(term[2:]) * 28 for term in terms}
    return [
        i + 1
        for i, privacy in enumerate(privacies)
        if convert_to_timestamp(privacy[:-2]) + terms[privacy[-1:]] <= today
    ]
