A,B,C = map(int,input().split())

if B>=C:   # 가변비용이 노트북 판매 비용보다 크면 이익이 날 수 없음
    print(-1)
else:
    print(int(A//(C-B)+1))   # 최초로 이익을 얻는 시점이므로 +1