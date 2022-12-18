import sys
from itertools import chain

if __name__ == '__main__':
    drs = ( 0, -1, -1, -1, 0, 1, 1, 1)
    dcs = (-1, -1,  0,  1, 1, 1, 0, -1)

    N, M = list(map(int, sys.stdin.readline().split()))
    A = []
    for _ in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))

    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    for _ in range(M):
        # Step 1
        visited = [[False] * N for _ in range(N)]
        d, s = list(map(int, sys.stdin.readline().split()))
        dr, dc = drs[d - 1], dcs[d - 1]
        clouds = [((c[0] + s * dr) % N, (c[1] + s * dc) % N) for c in clouds]
        offsets = []
        for r, c in clouds:
            # Step 2
            A[r][c] += 1
            visited[r][c] = True
            # Step 4
        for r, c in clouds:
            offset = 0
            if r == 0 and c == 0:
                offset += bool(A[r + 1][c + 1])
            elif r == 0 and c == N - 1:
                offset += bool(A[r + 1][c - 1])
            elif r == N - 1 and c == 0:
                offset += bool(A[r - 1][c + 1])
            elif r == N - 1 and c == N - 1:
                offset += bool(A[r - 1][c - 1])
            elif r == 0:
                offset += bool(A[r + 1][c - 1])
                offset += bool(A[r + 1][c + 1])
            elif r == N - 1:
                offset += bool(A[r - 1][c - 1])
                offset += bool(A[r - 1][c + 1])
            elif c == 0:
                offset += bool(A[r - 1][c + 1])
                offset += bool(A[r + 1][c + 1])
            elif c == N - 1:
                offset += bool(A[r - 1][c - 1])
                offset += bool(A[r + 1][c - 1])
            else:
                offset += bool(A[r - 1][c - 1])
                offset += bool(A[r - 1][c + 1])
                offset += bool(A[r + 1][c - 1])
                offset += bool(A[r + 1][c + 1])
            offsets.append(offset)
        for (r, c), o in zip(clouds, offsets):
            A[r][c] += o
        # Step 3
        clouds = []
        offsets = []
        # Step 5
        for r in range(N):
            for c in range(N):
                if visited[r][c]:
                    continue
                if A[r][c] >= 2:
                    A[r][c] -= 2
                    clouds.append((r, c))
    print(sum(chain.from_iterable(A)))
