# 프로그래머스 - 정수를 나선형으로 배치하기(181832)
# https://school.programmers.co.kr/learn/courses/30/lessons/181832


def move_right(row, col):
    return row, col + 1


def move_downward(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_upward(row, col):
    return row - 1, col


def solution(n):
    answer = [[0] * n for _ in range(n)]
    moves = [move_right, move_downward, move_left, move_upward]

    row, col = 0, 0
    current_move_index = 0
    for val in range(1, n**2 + 1):
        if (
            (row == 0 and col == n - 1)
            or (row == n - 1 and col == n - 1)
            or (row == n - 1 and col == 0)
            or answer[moves[current_move_index](row, col)[0]][
                moves[current_move_index](row, col)[1]
            ]
        ):
            current_move_index = (current_move_index + 1) % 4
        answer[row][col] = val
        row, col = moves[current_move_index](row, col)
    return answer
