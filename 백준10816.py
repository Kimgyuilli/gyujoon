import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

count = {}
for _ in card:
    if _ in count:
        count[_] += 1
    else:
        count[_] = 1
        

for _ in check:
    if _ in count:
        print(count[_], end = ' ')
    else:
        print(0, end = ' ')
