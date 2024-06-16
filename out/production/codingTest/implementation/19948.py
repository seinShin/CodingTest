# 19948 음유시인 영재
import sys
from string import ascii_lowercase
input = sys.stdin.readline

## 검사
def alpha_chk():
    ## 스페이스 검사
    if len(poem) -2 > space:
        return -1
    
    #poem 배열 문자 비교
    for sc in poem:
        for i in range(len(sc)):
            c = sc[i]
            if i == 0:
                alpha[c.lower()] -= 1
            else:
                if c==sc[i-1]:
                    continue
                else:
                    alpha[c.lower()] -=1
            if alpha[c.lower()] <=-1:
                return -1
    return True
            
            
## main
poem = input().strip().split()
space = int(input())
alphaArr = list(map(int, input().split()))

## 제목 구해서 append
title=''
for i in range(len(poem)):
    # print(poem[i][0].upper(), end='')
    title+= poem[i][0].upper()
poem.append(title)
        
## alpha dic 생성
alpha={}
for i in range(len(ascii_lowercase)):
    alpha[ascii_lowercase[i]] = alphaArr[i]
    
## 함수 실행
rst=alpha_chk()

## 결과
if rst == True:
    print(poem[-1])
else:
    print(-1)
    