# 2217 로프
import sys
input = sys.stdin.readline

n = int(input())

arr=[]
for _ in range(n):
    arr.append(int(input()))
    
arr.sort(reverse=True)

max = 0
for i in range(len(arr)):
    tmp = arr[i] * (i+1)
    if max < tmp:
        max = tmp
       
print(max)
    
    