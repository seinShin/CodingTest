# 1912 연속합
import sys
input = sys.stdin.readline

# 시간초과
# n = int(input())
# arr = list(map(int, input().split()))
# dp=[0]*n

# total = 0
# maxV=0
# for i in range(n):
#     total = arr[i]
#     for j in range(i+1, n):
#         total += arr[j]
#         if total > maxV :
#             maxV = total
#     dp[i] = maxV 
    

# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i]+arr[i-1])
    
print(max(arr))