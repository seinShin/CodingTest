# 9519 졸려
import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
word = list(input().strip())
start = ''.join(word)
#원래 입력값이 나올때까지 반복되는 문자배열 저장
rst=[]

while True:
    # 위치 변화 개수
    n = len(word) // 2
    stk=[]
    stk2=deque()
    
    # for문을 돌며 위치를 변화시켜야 하는 알파벳과 그렇지 않은 알파벳 검사
    for i in range(len(word)-1, -1, -1):
        alpha=word.pop()
        if i == (2*n)-1:
            stk.append(alpha)
            n-=1
        else:
            stk2.appendleft(alpha)
    word=list(stk2)+stk
    
    # 처음 입력값과 다르다면 rst에 append, 그렇지 않다면 종료
    if ''.join(word) != start:
        rst.append(''.join(word))
    else:
        rst.append(''.join(word))
        break
    
# rst의 길이가 1이라면 문자열의 알파벳이 모두 같으므로 그대로 출력
# 길이가 다르면 반복하는 횟수를 rst의 길이로 나눈 나머지-1이 인덱스인
# 배열 rst의 원소 출력
if len(rst) == 1:
    print(rst[0])
else:
    k = x%len(rst)
    print(rst[k-1])