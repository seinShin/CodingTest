# 4659 비밀번호 발음하기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

moum=['a', 'e', 'i', 'o', 'u']
yes = " is acceptable."
no = " is not acceptable."

while True:
    sts = True
    moumSts=False

    cnt1=0  # 모음
    cnt2=0  # 자음
    n = input().strip()
    
    if n == "end":
        break
    for i in range(len(n)):
        
        if i>0:
            if n[i] == n[i-1]:
                if n[i] != 'e' and n[i] != 'o':
                    sts = False
                    break
        
        if n[i] in moum:
            moumSts = True
            cnt2=0
            cnt1+=1
            
            if cnt1 == 3:
                sts = False
                break
        
        else:
            cnt1=0
            cnt2+=1
            if cnt2 == 3:
                sts = False
                break

    if not sts or moumSts == False:
        print("<"+n+">"+no)
    else:
        print("<"+n+">"+yes)
    
            
            
        
        
    
    