import sys

N = int(sys.stdin.readline())  # 테스트 케이스의 개수

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for i in range(1, len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[i] > line[j]:
                line[i], line[j] = line[j], line[i]
                sum += 1
            
    print(line[0], sum)
            