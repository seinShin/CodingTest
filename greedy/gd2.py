import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst=[]
for _ in range(n):
    lst.append(int(input()))
    
lst.sort(reverse=True)

cnt=0

for i in range(n):
    if lst[i] <= k:
        cnt += k //lst[i]
        k %= lst[i]
        if k<=0:
            break

print(cnt)
