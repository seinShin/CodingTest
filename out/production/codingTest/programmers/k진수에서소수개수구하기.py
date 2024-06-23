# # 2022 카카오 블라인드 채용 - k진수에서 소수 개수 구하기

# import math
# def change(n,k):
#     tmp = []
#     while n:
#         tmp.append(str(n % k)) 
#         n = n // k
#     return ''.join(tmp[::-1])
    
# def is_prime_number(num):
#     x=int(num)
#     if x == 1:
#         return False
    
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# def solution(n, k):
#     answer = 0
#     tmp = change(n,k)
    
#     num=''
#     for i in tmp:
#         if i != '0':
#             num+=i
#         else:
#             if num != '':
#                 if is_prime_number(num):
#                     answer+=1
#             num=''
#     if num != '':
#         if is_prime_number(num):
#             answer+=1
#     return answer

# 코드 리팩토링
# 기존 for문을 삭제하고 split을 이용하여 num 리스트 구함

import math

## n진법 변환 후 0으로 split한 리스트 출력
def change(n,k):
    tmp = []
    while n:
        tmp.append(str(n % k)) 
        n = n // k
    return ''.join(tmp[::-1]).split('0')
    
## 소수 판별 함수 - 에라토스테네스의 체 활용
def is_prime_number(num):
    x=int(num)
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

## main 함수
def solution(n, k):
    answer = 0
    tmp = change(n,k)
    for i in tmp:
        if i != '' and is_prime_number(i):
            answer+=1
    return answer