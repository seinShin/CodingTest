# 1058 친구
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
nlist=[[0]*n  for i in range(n)]

arr=[]
for _ in range(n):
    tmp = list(input())
    arr.append(tmp)

    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if arr[i][j] == "Y" or (arr[i][k]=='Y' and arr[k][j] == "Y"):
                nlist[i][j] = 1
                
cnt=0
for lst in nlist:
    cnt = max(cnt, sum(lst))
print(cnt)
