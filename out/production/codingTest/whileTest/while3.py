N = int(input())
T = N

cnt =0
while True:
    a=int(N/10)
    b=N%10
    c=a+b
    result=int(str(b)+str(c%10))
    cnt+=1
    if(result==T):
        break
    else:
        N = result
print(cnt)