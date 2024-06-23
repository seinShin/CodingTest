while True:
    tList = list(map(int,input().split()))
    
    a = max(tList)
    tList.remove(a)
    b = tList[0]
    c = tList[1]
    if(a ==0 and b==0 and c==0):
        break
    if(a*a == (b*b + c*c)):
        print("right")
    else:
        print("wrong")    