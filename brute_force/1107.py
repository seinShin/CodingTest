# 1107 리모컨  ---- 수정중
import sys
input = sys.stdin.readline


def numChk(x):
    cnt=1
    while True:
        if x+cnt not in xNum:
            return x+cnt
        if x-cnt not in xNum and x-cnt>=0:
            return x-cnt
        cnt+=1  
            
n = int(input())
m = int(input())
if m != 0:
    xNum=list(map(int, input().split()))
numList=[i for i in range(10)]

if n == 100:
    print(0)
elif m == 0:
    print(len(str(n)))
else:
    num = str(n)
    total=''
    sts="over"
    idx=0
    for i in range(len(num)):
        if int(num[i]) in xNum:
            rst = numChk(int(num[i]))
            if rst>=10:
                total+= num[i]
                break
            total+=str(rst)
            if int(num[i])>rst:
                sts="over"
                idx=i+1
                break
            else:
                sts="down"
                idx=i+1
                break
        else:
            total+=num[i]
            
    if sts =="over":
        numList.sort(reverse=True)

    if idx != 0:
        for i in numList:
            if i not in xNum:
                tempx=i
                break
        for i in range(idx,len(num)):
            total+=str(tempx)
   
        
    # print("---", total)
    
    if int(total)>n:
        print(len(num)+int(total)-n)
    elif n== int(total):
        if n> int(total):
            print(n-int(total))
        else:
            print(int(total)-n)
    else:
        print(len(num)+n-int(total))
            
        
        
    