# 17281 야구
from itertools import permutations
import sys
sys.stdin=open("input.txt")
n = int(input())
order = [[*map(int, input().split())] for _ in range(n)]
result=0
#인덱스
for taja in permutations((range(1,9)), 8):
    taja = list(taja[:3])+ [0] + list(taja[3:])
    
    current_idx = 0
    answer=0
    
    for i in range(n):
        out=0
        ru=[0,0,0,0]
        
        while out<3:
            
            # 현재 타자
            hit = order[i][taja[current_idx]]
            
            if hit == 0:
                out+=1
            elif hit == 1:
                answer += ru[3]
                ru=[0,1,ru[1], ru[2]]
            elif hit == 2:
                answer += ru[3] + ru[2]
                ru = [0,0,1,ru[1]]
            elif hit == 3:
                answer+=ru[3]+ru[2]+ru[1]
                ru=[0,0,0,1]
            elif hit == 4:
                answer+= ru[3]+ru[2]+ru[1]+1
                ru=[0,0,0,0]                
                
            current_idx = (current_idx+1)%9
            
        if answer >result:
            result = answer
            
print(result)





    
    




