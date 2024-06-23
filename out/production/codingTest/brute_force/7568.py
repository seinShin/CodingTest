# 7568 덩치
import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))
    
for i in lst:
    k=1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            k+=1
    
    print(k, end=" ")

