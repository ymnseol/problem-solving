# 프로그래머스 - [카카오 인턴] 보석 쇼핑(67258)
# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    left = 0
    right = 1
    all_gems = set(gems)
    curr_gems = set([gems[0]])
    n_gems = {gem: 0 for gem in all_gems}
    n_gems[gems[0]] += 1
    
    min_left = 0
    min_right = len(gems)
    min_len = len(gems)
    
    while left < right:
        if len(curr_gems) == len(all_gems):
            if right - left < min_len:
                min_left = left
                min_right = right
                min_len = right - left
            n_gems[gems[left]] -= 1
            if n_gems[gems[left]] == 0:
                curr_gems.discard(gems[left])
            left += 1
        elif right < len(gems):
            if n_gems[gems[right]] == 0:
                curr_gems.add(gems[right])
            n_gems[gems[right]] += 1
            right += 1
        else:
            break
    
    return [min_left + 1, min_right]
