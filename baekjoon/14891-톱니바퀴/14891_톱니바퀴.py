import sys

if __name__ == '__main__':
    gear = [list(map(int, list(sys.stdin.readline().rstrip()))) if g else [] for g in range(5)]
    k = int(sys.stdin.readline())
    rotation = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]

    for g, d in rotation:
        rotate = [0] * 5
        rotate[g] = d
        if g == 1:
            if gear[1][2] ^ gear[2][6]:
                rotate[2] = -d
            if rotate[2] and (gear[2][2] ^ gear[3][6]):
                rotate[3] = d
            if rotate[3] and (gear[3][2] ^ gear[4][6]):
                rotate[4] = -d
        elif g == 2:
            if gear[1][2] ^ gear[2][6]:
                rotate[1] = -d
            if gear[2][2] ^ gear[3][6]:
                rotate[3] = -d
            if rotate[3] and (gear[3][2] ^ gear[4][6]):
                rotate[4] = d
        elif g == 3:
            if gear[2][2] ^ gear[3][6]:
                rotate[2] = -d
            if gear[3][2] ^ gear[4][6]:
                rotate[4] = -d
            if rotate[2] and (gear[1][2] ^ gear[2][6]):
                rotate[1] = d
        elif g == 4:
            if gear[3][2] ^ gear[4][6]:
                rotate[3] = -d
            if rotate[3] and (gear[2][2] ^ gear[3][6]):
                rotate[2] = d
            if rotate[2] and (gear[1][2] ^ gear[2][6]):
                rotate[1] = -d
        for i, r in enumerate(rotate):
            if i and r:
                if r == -1:
                    gear[i] = gear[i][1:] + [gear[i][0]]
                elif r == 1:
                    gear[i] = [gear[i][-1]] + gear[i][:-1]
    
    print(sum([g[0] * (2 ** (i-1)) for i, g in enumerate(gear) if i]))
