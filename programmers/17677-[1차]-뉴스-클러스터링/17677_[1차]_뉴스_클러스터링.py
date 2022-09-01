# 프로그래머스 - [1차] 뉴스 클러스터링(17667)
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    intxn = sum([min(str1.count(c), str2.count(c)) for c in set(str1) & set(str2)])
    un = sum([max(str1.count(c), str2.count(c)) for c in set(str1) | set(str2)])
    
    if un:
        return int(intxn / un * 65536)
    return 65536
