# 10825 국영수
import sys
input = sys.stdin.readline

n = int(input())
arr=[]

for i in range(n):
    lst = list(map(str, input().split()))
    arr.append(lst)
    

arr.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for lst in arr:
    print(lst[0])