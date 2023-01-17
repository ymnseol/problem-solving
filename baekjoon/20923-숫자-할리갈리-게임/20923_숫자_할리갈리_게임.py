# 백준 - 숫자 할리갈리 게임(20923)
# https://www.acmicpc.net/problem/20923

import sys
from collections import deque

if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    do_deck = deque()
    su_deck = deque()
    for _ in range(N):
        d, s = list(map(int, sys.stdin.readline().split()))
        do_deck.appendleft(d)
        su_deck.appendleft(s)
    do_ground = deque()
    su_ground = deque()
    for i in range(M):
        if i % 2 == 0:
            do_ground.append(do_deck.popleft())
        else:
            su_ground.append(su_deck.popleft())
        if not do_deck or not su_deck:
            break
        if (do_ground and do_ground[-1] == 5) or (su_ground and su_ground[-1] == 5):
            do_deck.extend(su_ground)
            do_deck.extend(do_ground)
            do_ground = deque()
            su_ground = deque()
        elif do_ground and su_ground and (do_ground[-1] + su_ground[-1] == 5):
            su_deck.extend(do_ground)
            su_deck.extend(su_ground)
            do_ground = deque()
            su_ground = deque()
    if len(do_deck) > len(su_deck):
        print("do")
    elif len(do_deck) < len(su_deck):
        print("su")
    else:
        print("dosu")
