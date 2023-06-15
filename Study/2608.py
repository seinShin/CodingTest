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

#숫자_문자
def num_to_str(num):
    roma=''
    i=0
    # 자리수와 숫자 체크 
    while num!=0:
        size=len(str(num))
        k=int(str(num)[i])
        
        if 4== size:
            roma+= 'M'*k
            num -= 1000*k
        elif size==3:
            if 9 == k:
                roma +='CM'
                num-=900
            elif 5<=k<9:
                roma += 'D'
                num-=500
            elif 4<=k<5:
                roma += 'CD'
                num-= 400
            else: 
                roma += 'C'
                num-=100
        elif size==2:
            if 9 == k:
                roma +='XC'
                num-=90
            elif 5<=k<9:
                roma += 'L'
                num-=50
            elif 4<=k<5:
                roma += 'XL'
                num-= 40
            else: 
                roma += 'X'
                num-=10
        else:
            if 9 == k:
                roma +='IX'
                num-=9
            elif 5<=k<9:
                roma += 'V'
                num-=5
            elif 4<=k<5:
                roma += 'IV'
                num-= 4
            else: 
                roma += 'I'
                num-=1
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
