# 프로그래머스 - 바탕화면 정리(161990)
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

from itertools import chain


def solution(wallpaper):
    grids = list(chain.from_iterable(wallpaper))
    file_indices = list(
        map(
            lambda i: (i // len(wallpaper[0]), i % len(wallpaper[0])),
            list(filter(lambda i: grids[i] == "#", range(len(grids)))),
        )
    )
    vertical_file_indices = sorted(file_indices, key=lambda x: x[1])
    l = vertical_file_indices[0][1]
    u = file_indices[0][0]
    r = vertical_file_indices[-1][1] + 1
    d = file_indices[-1][0] + 1
    return [u, l, d, r]
