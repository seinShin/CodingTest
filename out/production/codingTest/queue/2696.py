# 2696 중앙값 구하기
import sys, heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    data=[]
    
    for i in range(m//10+1):
        data.extend(list(map(int, input().split())))
    
    left=[]    #중앙값보다 작은 수
    right=[]   #중앙값보다 큰 수
    mid=data[0] #첫번째 중앙값
    answer=[mid]    #결과값
    
    for i in range(1,m):
        if data[i] <= mid:
            heapq.heappush(left, -data[i])
        else:
            heapq.heappush(right, data[i])
            
        if i%2 == 0:
            if len(left)>len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(left)<len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            answer.append(mid)
    
    
    # 10개씩 끊어서 출력
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=' ')
        if(i+1) % 10 == 0:
            print()
   
    
    