# 프로그래머스 - 구명보트(42885)
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    cnt = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1
    
    return cnt
