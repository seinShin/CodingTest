# 1026 보물

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

s=0
for i in range(len(a)):
    s += a[i]*b[i]
    
print(s)