N = int(input())
coor = []
for _ in range(N):
    a, b = input().split()
    coor.append([_, int(a), b])
coor.sort(key=lambda x: (x[1], x[0])) #두번째 거를 내림차순으로 하고싶으면 -x[0]으로 입력

for i in range(N):
    print(coor[i][1], coor[i][2]) 