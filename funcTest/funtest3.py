def numList(s):   #각 자리수 분리 함수
    num=[]
    for i in str(s):
        num.append(i)
    return  num

N=int(input())
cnt=0

for i in range(1,N+1):
    num = numList(i)
    if len(num)==1 or len(num)==2:
        cnt+=1
    elif len(num)==3:
        if((int(num[1])-int(num[0])) == (int(num[2])-int(num[1]))):
            cnt+=1
    elif len(num)==4:
        if((int(num[3])-int(num[2])) == (int(num[2])-int(num[1]))== (int(num[1])-int(num[0]))):
            cnt+=1    
print(cnt)




