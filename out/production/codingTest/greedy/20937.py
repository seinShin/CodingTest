# 20937 떡국
import sys
input = sys.stdin.readline

n = int(input())
lst = [*map(int, input().split())]
tops= [0]*500001
for i in lst:
    tops[i] += 1
        
print(max(tops))