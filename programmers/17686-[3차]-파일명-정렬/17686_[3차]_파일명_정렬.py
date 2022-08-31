# 프로그래머스 - [3차] 파일명 정렬(17686)
# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    sorted_files = []
    for i, file in enumerate(files):
        file = file.lower()
        head = re.search(r'^([^\d]+)', file)
        if head:
            head = head.group(0)
        number = re.search(r'[0-9]+', file)
        if number:
            number = number.group(0)
        sorted_files.append((head, int(number), i))
    sorted_files.sort()
    return [files[i] for _, _, i in sorted_files]
