import sys
input = sys.stdin.readline

N, M = map(int, input().split())

count1 = set()
for _ in range(N):
    count1.add(input().strip())
count2 = set()
for _ in range(M):
    count2.add(input().strip())
result = sorted(list(count1 & count2))

print(len(result))
for _ in result:
    print(_)
    
    

