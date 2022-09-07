# 프로그래머스 - k진수에서 소수 개수 구하기(92335)
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    cnt = 0
    new_n = ''

    while n:
        new_n = str(n % k) + new_n
        n //= k
    
    new_n = [int(p) for p in new_n.split('0') if p and int(p) > 1]
    
    for p in new_n:
        for d in range(2, int(p ** 0.5) + 1):
            if p % d == 0:
                break
        else:
            print(p)
            cnt += 1

    return cnt
