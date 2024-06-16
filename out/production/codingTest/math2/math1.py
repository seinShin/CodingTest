#소수판별 함수
def priTest(n):
    i=1
    rst=0
    while i*i<n:
        if n%i ==0:
            rst +=2
        i+=1
    if i*i == n:
        rst +=1
    return rst
    
N=int(input())

a = list(map(int, input().split()))   #한줄에 공백으로 나눠서 여러 숫자 입력 ->list로 받기
con = 0;
for x in a:
    if priTest(x) == 2:
          con +=1

print(con) 
    

