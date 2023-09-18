# 13458 시험 감독
import sys
input = sys.stdin.readline

n = int(input())
people=list(map(int, input().split()))
b,c = map(int, input().split())
total = b+c


ans=0
for i in range(len(people)):
    if people[i] <= total:
        if people[i] <= b:
            ans += 1
        else:
            ans+=2
    else:
        tmp = (people[i]-total) 
        ans+=2
        ans+= tmp//c
        if tmp%c:
            ans+=1
        
print(ans)
    