# 숫자 재배치
from itertools import permutations
import sys
input = sys.stdin.readline


a, b = map(int, input().split())
maxNum = -1
sa = str(a)

for com in permutations(sa, len(sa)):
    x = ''.join(com)
    print(x)
    if x[0] == "0":
        continue
    x=int(x)
    if x < b:
        maxNum =max(maxNum, x)

print(maxNum)
    
