# 9241 바이러스 복제 -----미해결
import sys

n = list(input().strip())
k = list(input().strip())

i=0
while True:
    if n[i] != k[i] or i == len(n)-1 or i == len(k)-1:
        break 
    
    i+=1
    

j=-1
while True:
    if n[j] != k[j] or len(n)+j == 0 or len(k)+j == 0:
        break
    
    j-=1


rst=len(k)+j-i+1
if len(n)>len(k):
    if n[:i]+n[j+1:] == k:
        print(0)
    else:
        if len(k) == 1:
            print(0)
        else:
            if len(n)+j > i:
                print(len(n)+j-i-1)
            else:
                print(i-(len(n)+j))    
else:
    if len(n) == 1:
        print(len(k)+j-i)
    else:
        print(len(k)+j-i+1)