# 1063 킹
import sys
input = sys.stdin.readline

king, rock, n = map(str, input().strip().split())

# 좌표 딕셔너리
moveDic = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1],
        'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

# 알파벳 - 숫자 딕셔너리
arr={"A": 1, "B": 2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}

king = [arr[king[0]],int(king[1])]
rock = [arr[rock[0]],int(rock[1])]


for i in range(int(n)):
    move = input().strip()
    
    x,y=moveDic[move]
    
    k_x = king[0]+x
    k_y = king[1]+y
        
    # king - 범위 검사
    if 0<k_x<=8 and 0<k_y<=8:
        if k_x == rock[0] and k_y == rock[1]:
            r_x = rock[0]+x
            r_y = rock[1]+y
            
            # rock - 범위 검사
            if 0<r_x<=8 and 0<r_y<=8:
                king=[k_x, k_y]
                rock=[r_x, r_y]
        else:
            king=[k_x, k_y]
     
## 결과값 : 숫자 - 알파벳 변환   
for key, value in arr.items():
    if king[0] == value:
        k_x = key
        
    if rock[0] == value:
        r_x = key
        
print(k_x+str(king[1]))
print(r_x+str(rock[1]))