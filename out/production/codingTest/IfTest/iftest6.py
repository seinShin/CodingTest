## 오븐시계

n,m = map(int, input().split())
k = int(input())
if m+k >= 60:
    n = n+ ((m+k)// 60)
    if n>= 24:
        n -=24    
    print(n, (m+k)%60)
else:
    print(n, m+k)