import sys

input = sys.stdin.readline

N, M = map(int, input().split())
Nlist = {}
for _ in range(1, N + 1):
    inp = input().strip()
    Nlist[_] = inp
    Nlist[inp] = _

for _ in range(M):
    A = input().strip()
    if A.isdecimal():
        print(Nlist[int(A)])
    else:
        print(Nlist[A])
    