import sys

JipHap = {}
M = int(sys.stdin.readline())

for _ in range(M):
    inputs = sys.stdin.readline().split()
    Calcul = inputs[0]
    
    if Calcul in {"add", "remove", "check", "toggle"}:
        Num = int(inputs[1]) 
    if Calcul == "add":
        if Num not in JipHap:
            JipHap[Num] = 0
    
    elif Calcul == "remove":
        if Num in JipHap:
            del JipHap[Num]
    
    elif Calcul == "check":
        if Num in JipHap:
            print(1)
        else:
            print(0)
    
    elif Calcul == "toggle":
        if Num in JipHap:
            del JipHap[Num]
        else:
            JipHap[Num] = 0
    
    elif Calcul == "all":
        JipHap = {i: 0 for i in range(1, 21)}
    
    elif Calcul == "empty":
        JipHap.clear()
