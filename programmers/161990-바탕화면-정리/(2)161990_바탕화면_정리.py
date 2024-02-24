# 프로그래머스 - 바탕화면 정리(161990)
# https://school.programmers.co.kr/learn/courses/30/lessons/161990


def solution(wallpaper):
    file_row_indices = []
    file_col_indices = []
    for row_index, row in enumerate(wallpaper):
        col_left_index = row.find("#")
        col_right_index = row.rfind("#")
        if col_left_index != -1:
            file_row_indices.append(row_index)
            file_col_indices.append(col_left_index)
        if col_right_index != -1:
            file_row_indices.append(row_index)
            file_col_indices.append(col_right_index)
    return [
        min(file_row_indices),
        min(file_col_indices),
        max(file_row_indices) + 1,
        max(file_col_indices) + 1,
    ]
