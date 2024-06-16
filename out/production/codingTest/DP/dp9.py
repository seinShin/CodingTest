import sys
n = int(sys.stdin.readline())
lst= [*map(int, sys.stdin.readline().split())]

for i in range(1,n):
    lst[i] = max(lst[i], lst[i]+lst[i-1])
    
print(max(lst))

    