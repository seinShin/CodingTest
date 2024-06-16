# 3048 개미
import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
n1= list(input().strip())
n2= list(input().strip())

n1.reverse()
total=n1+n2
t = int(input())
for _ in range(t):
    for i in range(len(total)-1):
        if total[i] in n1 and total[i+1] in n2:
            total[i], total[i+1] = total[i+1], total[i]
            if total[i+1] == n1[-1]:
                break
        
print("".join(total))