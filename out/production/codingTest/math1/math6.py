for _ in range(int(input())):
    f = int(input())
    n = int(input())
    fList = [x for x in range(1,n+1)]
    for k in range(f):
        for i in range(1,n):
            fList[i] += fList[i-1]
    print(fList[-1])