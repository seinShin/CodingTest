# 2608 로마 숫자
import sys
input = sys.stdin.readline

#참고 딕셔너리
l1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
l2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

#문자_숫자
def str_to_num(romaList):
    total=0
    i=0
    while romaList:
        
        if len(romaList)==1:
            total += l1[romaList[i]]
            break
        
        plus = romaList[i]+romaList[i+1]
        if plus in l2:
            total+=l2[plus]
            romaList=romaList[i+2:]
        else:
            total+=l1[romaList[i]]
            romaList=romaList[i+1:]
            
    return total

op = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 
      'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

#숫자_문자
def num_to_str(num):
    times = {'M': 3, 'CM': 1, 'D': 1, 'CD': 1, 'C': 3, 'XC': 1, 
      'L': 1, 'XL': 1, 'X': 3, 'IX': 1, 'V': 1, 'IV': 1, 'I': 3}    
    word = []
    for t in times:
        value = op.get(t) # 뺄 숫자
        limit = times[t]
        while limit and num >= value:
            num -= value
            times[t] -= 1
            word.append(t)
    return ''.join(word)

    # roma=''
    # i=0
    # # 자리수와 숫자 체크 
    # while num!=0:
    #     size=len(str(num))
    #     k=int(str(num)[i])
        
    #     if 4== size:
    #         roma+= 'M'*k
    #         num -= 1000*k
    #     elif size==3:
    #         if 9 == k:
    #             roma +='CM'
    #             num-=900
    #         elif 5<=k<9:
    #             roma += 'D'
    #             num-=500
    #         elif 4<=k<5:
    #             roma += 'CD'
    #             num-= 400
    #         else: 
    #             roma += 'C'
    #             num-=100
    #     elif size==2:
    #         if 9 == k:
    #             roma +='XC'
    #             num-=90
    #         elif 5<=k<9:
    #             roma += 'L'
    #             num-=50
    #         elif 4<=k<5:
    #             roma += 'XL'
    #             num-= 40
    #         else: 
    #             roma += 'X'
    #             num-=10
    #     else:
    #         if 9 == k:
    #             roma +='IX'
    #             num-=9
    #         elif 5<=k<9:
    #             roma += 'V'
    #             num-=5
    #         elif 4<=k<5:
    #             roma += 'IV'
    #             num-= 4
    #         else: 
    #             roma += 'I'
    #             num-=1
    return roma



# 입력
n1=input().strip()
n2=input().strip()

# 아라비아 출력
num1=str_to_num(n1)
num2= str_to_num(n2)
print(num1+num2)

# 로마 출력
romaNum=num_to_str(num1+num2)
print(romaNum)
