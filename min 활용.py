N = sorted(list(map(int, input().split())))

if N[0]+N[1] <= N[2]:
    N[2] = N[0]+N[1]-1
# res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(sum(N))