# 프로그래머스 - N으로 표현(42895)
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        num = int(str(N) * i)
        if num == number:
            return i
        dp[i].add(num)
        for j in range(1, i // 2 + 1):
            for n1 in dp[j]:
                for n2 in dp[i - j]:
                    if n1 + n2 == number:
                        return i
                    if n1 - n2 == number:
                        return i
                    if n2 - n1 == number:
                        return i
                    if n1 * n2 == number:
                        return i
                    if n2 and n1 // n2 == number:
                        return i
                    if n1 and n2 // n1 == number:
                        return i
                    
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n2 - n1)
                    dp[i].add(n1 * n2)
                    if n2:
                        dp[i].add(n1 // n2)
                    if n1:
                        dp[i].add(n2 // n1)
    
    return -1
