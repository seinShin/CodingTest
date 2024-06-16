import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
sumL = [0]*(n+1)
cnt = [0]*(m+1)

for i in range(n):
    sumL[i+1] = (arr[i]+sumL[i])%m
    cnt[sumL[i+1]] +=1

ans = cnt[0]

for i in range(m+1):
    ans += (cnt[i]*(cnt[i]-1))//2
    
print(ans)