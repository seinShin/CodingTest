import sys
input = sys.stdin.readline

n = int(input())
lst=[*map(int, input().split())]
    
lst.sort()
min =0

for i in range(len(lst)):
    for j in range(i+1):
        min += lst[j]

print(min)