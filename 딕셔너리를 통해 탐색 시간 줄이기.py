import sys

A = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
C = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().split()))

_dict = {}
for i in range(A):
    _dict[B[i]] = 0 # 딕셔너리를 사용하여 탐색 시간 줄이기

for _ in range(C):
    if D[_] in _dict:
        print(1, end = ' ')
    else: print(0, end = ' ')
