# 7490 0 만들기
from itertools import product
import sys

input = sys.stdin.readline

#아스키 코드 값으로 정렬 하려먼 공백-> + -> -
sign=[' ', '+', '-']

for _ in range(int(input())):
    
    # 오름차순 리스트
    numList = [ i for i in range(1, int(input())+1)]

    # 부호에 대한 중복 순열 리스트, 각 케이스 별로 0이 되는지를 체크
    for s in product(sign, repeat=len(numList)-1):
        total=''
        s = list(s)
        
        # 숫자와 문자가 합쳐진 전체 문자열 total 생성
        for i in range(len(s)):
            total+=str(numList[i])
            total+=s[i]
        total+=str(numList[-1])
        
        # 공백 없앨 때 replace
        # eval 함수? -> 정리해놓기(eval/exec/compile)
        if eval(total.replace(' ', '')) == 0:
            print(total)
        
    print()
        
        
        
