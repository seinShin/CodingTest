import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst=[]
lst2=[]

for _ in range(n):
    lst.append(input())
for _  in range(m):
    lst2.append(input())
    
cnt=0
for i in lst2:
    if i in lst:
        cnt +=1
print(cnt)