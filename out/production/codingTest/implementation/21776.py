# 21776 가희와 읽기 쓰기 놀이 ----- 미해결
from itertools import permutations
import sys
input = sys.stdin.readline

def card_chk(order):
    state=True
    for i in range(len(order)):
        x = cardNum[order[i]]
        visit=[-1]*(len(order)+1)
        for j in range(order[i]):
            if cardNum[j] == x:
                state = False
            visit[order[i]] = 0
    return state
    

def get_string():
    total=[]
    flag=True
    # 순서 순열
    for order in permutations(range(1,c+1), c):
        c_string=''
        order=list(order)
        print("order=", order)
        print(card_chk(order))
        for i in range(len(order)):
            # 카드에 대한 식
            operation = cardOper[order[i]]
            # print("op,", operation)
            for oper in operation:
                oper=list(oper.split())
                if oper[0] == "ADD":
                    c_string += oper[1]
                else:
                    if int(oper[1]) >= len(c_string):
                        total.append("ERROR")
                        flag=False
                        break
                    else:
                        c_string=c_string[:int(oper[1])]+c_string[int(oper[1])+1:]
            
        if flag == False:
            break
        total.append(c_string)
    return total


## main
n,c = map(int, input().split())

#플레이어의 카드 순서
cardNum =[[] for _ in range(c+1)]  
# cardOper=[[] for _ in range(c+1)]
player=[i for i in range(1, n+1)]
cardOper={ idx: '' for idx in player}

for i in range(n):
    lst = list(map(int, input().split()))
    
    for j in range(1, len(lst)):
        cardNum[lst[j]] = i+1
        
    # cardNum[i+1] = lst[1:]
for i in range(c):
    operation = input().strip().split(',')
    cardOper[i+1] =operation

 
print(cardNum)
# print(cardOper)    

rst = get_string()
            
if rst == 0:
    print("EMPTY")
else:
    rst=list(set(rst))
    rst.sort()
    for i in rst:
        print(i)