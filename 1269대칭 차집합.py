import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res1 = list(A - B)
res2 = list(B - A)

print(len(res1)+len(res2))

123456

