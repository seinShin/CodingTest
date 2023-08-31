# 1010 다리 놓기
import sys
input = sys.stdin.readline


def fact(n):
    f=1
    for i in range(n):
        f *= (i+1)
    return f
        
    

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(fact(m) // (fact(m-n) * fact(n)))
