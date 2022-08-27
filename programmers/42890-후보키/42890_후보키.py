# 프로그래머스 - 후보키(42890)
# https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    keys = range(len(relation[0]))
    candidate_keys = set()
    
    for n_keys in range(1, len(relation[0]) + 1):
        # Check the uniqueness
        for key_c in combinations(keys, n_keys):
            tuples = set()
            for row in relation:
                pair = tuple([row[int(key)] for key in key_c])
                if pair in tuples:
                    break
                else:
                    tuples.add(pair)
            else:
                # Check the minimality
                for key in candidate_keys:
                    if set(key).issubset(set(key_c)):
                        break
                else:
                     candidate_keys.add(key_c)

    return len(candidate_keys)
