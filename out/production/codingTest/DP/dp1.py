import sys
cnt1=1
cnt2=0
def fibo(n):
    global cnt1
    if n==1 or n==2:
        return 1
    else:
        cnt1 +=1
        return (fibo(n-1)+fibo(n-2));
    
def dp(n):
    global cnt2
    f=[0 for i in range(41)]
    f[1] = 1;
    f[2] = 2;
    for i in range(3,n+1):
        cnt2+=1
        f[i] = f[i-1]+f[i-2]

k = int(sys.stdin.readline())
fibo(k)
dp(k)

print(cnt1, cnt2)
    