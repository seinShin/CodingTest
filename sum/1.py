import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst=[*map(int,input().split())]
sumList=[0]

cnt=0

for i in lst:
    cnt += i
    sumList.append(cnt)
    
for i in range(m):
    a,b = map(int, input().split())
    print(sumList[b]-sumList[a-1])