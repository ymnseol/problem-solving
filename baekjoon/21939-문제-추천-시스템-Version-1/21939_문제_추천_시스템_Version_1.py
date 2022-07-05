# 백준 - 문제 추천 시스템 Version 1(21939)
# https://www.acmicpc.net/problem/21939

import heapq

class SimpleHeap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.list = dict()
        self.s = dict()

    def add(self, P, L):
        heapq.heappush(self.min_heap, (L, P))
        heapq.heappush(self.max_heap, (-L, -P))
        self.list[P] = L

    def recommend(self, descending=False):
        if descending:
            l, p = -self.max_heap[0][0], -self.max_heap[0][1]
            while p in self.s and l == self.s[p]:
                heapq.heappop(self.max_heap)
                l, p = -self.max_heap[0][0], -self.max_heap[0][1]
        else:
            l, p = self.min_heap[0][0], self.min_heap[0][1]
            while p in self.s and l == self.s[p]:
                heapq.heappop(self.min_heap)
                l, p = self.min_heap[0][0], self.min_heap[0][1]
        return p

    def solved(self, P):
        self.s[P] = self.list[P]

if __name__ == '__main__':
    N = int(input())

    heap = SimpleHeap()

    for _ in range(N):
        P, L = map(int, input().split())
        heap.add(P, L)
    
    M = int(input())

    for _ in range(M):
        cmd = input().split()
        if cmd[0] == 'add':
            heap.add(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'recommend':
            if cmd[1] == '1':
                print(heap.recommend(descending=True))
            else:
                print(heap.recommend())
        else: # solved
            heap.solved(int(cmd[1]))
