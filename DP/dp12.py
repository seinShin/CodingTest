import sys
n = int(sys.stdin.readline())
lst=[*map(int, sys.stdin.readline().split())]
dp =[0]*len(lst)

for i in range(len(lst)):
    num=0
    pv=lst[i]
    for j in range(i+1, len(lst)):
        if pv < lst[j]:
            num+=1
            pv = lst[j]
    dp[i] = num+1
print(dp)
print(max(dp))