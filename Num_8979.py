N, K = map(int, input().split())
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

# 금, 은, 동 순으로 정렬하기 위한 비교 정렬
for i in range(N):
    for j in range(i + 1, N):
        if li[i][1] < li[j][1]:
            li[i], li[j] = li[j], li[i]
        elif li[i][1] == li[j][1]:
            if li[i][2] < li[j][2]:
                li[i], li[j] = li[j], li[i]
            elif li[i][2] == li[j][2]:
                if li[i][3] < li[j][3]:
                    li[i], li[j] = li[j], li[i]

# 팀 순위 계산
rank = [0] * N  # 각 팀의 순위를 저장할 리스트
current_rank = 1  # 현재 순위
rank[0] = 1  # 첫 번째 팀은 1등
for i in range(1, N):
    # 메달이 모두 같으면 같은 순위 부여
    if li[i][1:] == li[i-1][1:]:
        rank[i] = current_rank
    else:
        current_rank = i + 1
        rank[i] = current_rank

# K번 팀의 순위 출력
# K번 팀의 번호는 li에서 팀번호로 인덱싱되므로 인덱스 찾기
for i in range(N):
    if li[i][0] == K:
        print(rank[i])
        break