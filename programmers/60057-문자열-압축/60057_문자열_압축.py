# 프로그래머스 - 문자열 압축(60057)
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    min_len = len(s)
    
    for i in range(1, len(s)):
        pieces = [s[j:j+i] for j in range(0, len(s), i)]
        zipped = []
        
        curr = ''
        cnt = 1
        
        for w in pieces:
            if w == curr:
                cnt += 1
            else:
                zipped.append(str(cnt))
                zipped.append(curr)
                curr = w
                cnt = 1
        else:
            zipped.append(str(cnt))
            zipped.append(curr)
            
        min_len = min(min_len, len(''.join([c for c in zipped if c != '1'])))

    return min_len
