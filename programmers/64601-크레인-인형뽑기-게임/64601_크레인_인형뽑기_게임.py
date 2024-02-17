# 프로그래머스 - 크레인 인형뽑기 게임(64601)
# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    answer = 0
    columns = list(
        map(
            lambda col: list(reversed([element for element in col if element])),
            zip(*board),
        )
    )
    stack = []
    for move in moves:
        if not columns[move - 1]:
            continue
        stack.append(columns[move - 1].pop())
        if len(stack) > 1 and stack[-1] == stack[-2]:
            del stack[-2:]
            answer += 2
    return answer
