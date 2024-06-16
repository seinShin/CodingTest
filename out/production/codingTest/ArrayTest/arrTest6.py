N = int(input())
for i in range(N):
    arr=input()
    score=0   #전체 획득 점수
    cnt=0       # 구분하는 점수 
    for j in range(len(arr)):
        if arr[j] == 'O':
            cnt+=1
            score += cnt
        elif arr[j] =='X':
            score+=0
            cnt=0
    print(score)
            