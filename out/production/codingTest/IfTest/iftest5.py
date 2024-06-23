# 기준 = 45

H, M = map(int,input().split())

if(M<45):
    M = 60-(45-M)
    if(H==0):
        H = 23
    else:
        H = H-1
    print(H, M)
else:
    M = M-45
    print(H, M)

