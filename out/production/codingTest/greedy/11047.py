# 11047 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []

for _ in range(n):
    num = int(input())
    arr.append(num)
    
arr.sort(reverse=True)

min=0
for i in range(len(arr)):
    if arr[i] <= k:
        min += k // arr[i]
        k %= arr[i]
        
        if k<0:
            break  
print(min)
        
    