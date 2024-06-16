#1759 암호 만들기
from itertools import combinations
import sys

input = sys.stdin.readline

l,c = map(int, input().split())
alpa = list(map(str, input().strip().split()))
rst=[]

#조합 이용
for lst in combinations(alpa, l):
    cnt=0
    for i in lst:
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt+=1   
    if 1<=cnt and cnt<=l-2:
        x = list(lst)
        x.sort()
        rst.append(x)
# 정렬
rst.sort()
for i in rst:
    i.sort()
    for j in i:
        print(j, end="")
    print()