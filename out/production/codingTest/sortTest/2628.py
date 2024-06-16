# 2628 종이자르기
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

row=[0,n]
col=[0,m]

for i in range(int(input())):
    dir, dot = map(int, input().split())
    
    if dir == 0:
        col.append(dot)
    else:
        row.append(dot)
        
row.sort()
col.sort()

sub1=[]
sub2=[]
for i in range(len(row)-1):
    sub1.append(row[i+1]-row[i])
for i in range(len(col)-1):
    sub2.append(col[i+1]-col[i])
    
print(max(sub1)*max(sub2))
     

    
    
    
    