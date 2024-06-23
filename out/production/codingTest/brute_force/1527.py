# 1527 금민수의 개수
import sys
from itertools import product

input = sys.stdin.readline

a,b = map(int, input().split())
ax = len(str(a))
bx = len(str(b))

cnt=0
for i in range(ax, bx+1):
    lst= list(product(["4","7"], repeat=i))
    for x in lst:
        tmp=int(''.join(list(x)))
        if a<=tmp <=b:
            cnt+=1
print(cnt)
    