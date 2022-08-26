# 프로그래머스 - [3차] 방금그곡(17683)
# https://school.programmers.co.kr/learn/courses/30/lessons/17683

import re
import heapq

def solution(m, musicinfos):
    pq = []
    
    # Preprocess m
    sharp = {'C#': 'V', 'D#': 'W', 'F#': 'X', 'G#': 'Y', 'A#': 'Z'}
    m = re.findall(r'[A-Z]{1}#{0,1}', m)
    for i, c in enumerate(m):
        if sharp.get(c):
            m[i] = sharp[c]
    m = ''.join(m)
    
    # Preprocess the music played
    for info in musicinfos:
        time = int(info[6:8]) * 60 + int(info[9:11]) - int(info[0:2]) * 60 - int(info[3:5])
        _, _, name, melody = info.split(',')
        melody = re.findall(r'[A-Z]{1}#{0,1}', melody)
        for i, note in enumerate(melody):
            if sharp.get(note):
                melody[i] = sharp[note]
        full_music = ''
        for i in range(time):
            full_music += melody[i % len(melody)]
        heapq.heappush(pq, (-time, name, full_music))

    # Find the music
    while pq:
        time, name, music = heapq.heappop(pq)
        if m in music:
            return name
    return "(None)"
