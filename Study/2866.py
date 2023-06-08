import sys
input = sys.stdin.readline

r,c = map(int, input().strip().split())
lst = [ str(input().strip()) for _ in range(r)]

chkList=['' for _ in range(c)]
answer=r-1

while lst:
    dic={}
    flag = False
    x = lst.pop()
    for i in range(c):
        if dic.get(chkList[i]+x[i]) is None:
            chkList[i] = chkList[i]+x[i]
            dic[chkList[i]]=1
            
        else:
            chkList[i] = chkList[i]+x[i]
            flag = True
    if flag:
        answer -= 1
        
        
print(answer)