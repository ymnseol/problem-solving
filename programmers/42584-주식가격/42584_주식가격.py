# 프로그래머스 - 주식가격(42584)
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
        else:
            answer.append(len(prices) - i - 1)
    return answer
