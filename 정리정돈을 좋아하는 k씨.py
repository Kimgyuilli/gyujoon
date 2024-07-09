n, M = map(int, input().split())
li = list(map(int, input().split()))
for _ in range(M):
    StartRn, EndRn, Sel = map(int, input().split())
    work = li[StartRn-1:EndRn]
    work.sort()
    print(work[Sel-1])
    
