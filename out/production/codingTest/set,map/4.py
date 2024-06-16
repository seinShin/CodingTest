import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = set()
for i in range(n):
    lst.add(input())
lst2=set()
for j in range(m):
    lst2.add(input())
    
rst = sorted(list(lst&lst2))
print(len(rst))
print(*rst, sep='')  