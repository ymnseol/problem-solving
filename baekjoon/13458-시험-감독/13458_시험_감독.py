import sys
from math import ceil

N = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().split())
B, C = map(int, sys.stdin.readline().split())

print(N + sum([ceil((a - B) / C) for a in A if a > B]))
