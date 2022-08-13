# 프로그래머스 - 베스트앨범(42579)
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []

    songs = [(genres[i], plays[i], i) for i in range(len(genres))]

    by_genre = dict()
    for i in range(len(genres)):
        try:
            by_genre[genres[i]] += plays[i]
        except:
            by_genre[genres[i]] = plays[i]
    by_genre = dict(sorted(by_genre.items(), key=lambda item: item[1], reverse=True))
    
    songs = sorted(songs, key=lambda item: (by_genre[item[0]], item[1], -item[2]), reverse=True)
    
    curr = songs[0][0]
    cnt = 0
    
    for s in songs:
        if s[0] != curr:
            curr = s[0]
            cnt = 0
        if s[0] == curr and cnt < 2:
            cnt += 1
            answer.append(s[2])

    return answer
