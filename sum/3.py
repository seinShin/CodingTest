import sys
input = sys.stdin.readline

s = input().strip()

for _ in range(int(input())):
    a,l,r = map(str, input().strip().split())
    
    cnt=0
    for i in range(int(l),int(r)+1):
        if s[i] == a:
            cnt+=1
            
    print(cnt)   
    
    