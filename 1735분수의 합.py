import math
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = {}
c[0] = a[0]*b[1] + a[1]*b[0]
c[1] = a[1] * b[1]
if(math.gcd(c[0], c[1])):
    print(int(c[0]/math.gcd(c[0],c[1])), int(c[1]/math.gcd(c[0],c[1])))
else: print(c[0], c[1])
