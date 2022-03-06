for _ in range(int(input())):
    H,W,N = map(int, input().split())
    p = N%H
    b = N//H +1
    if p ==0:
        p=H
        b-=1
    print(p*100+b)