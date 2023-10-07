# 1004 어린 왕자
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1,y1,x2,y2 = map(int, input().split())
    cnt=0
    n = int(input())
    for _ in range(n):
        cx,cy,r = map(int, input().split())
        d1 = (x1-cx)**2+(y1-cy)**2
        d2 = (x2-cx)**2+(y2-cy)**2
        r = r**2
        
        if r>d1 and r>d2:
            pass
        elif r > d1:
            cnt+=1
        elif r >d2:
            cnt+=1
           
    print(cnt)