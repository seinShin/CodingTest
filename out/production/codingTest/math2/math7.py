from cmath import sqrt
import math
x,y,w,h = map(int, input().split())
num1 = h-y
num2 = w-x
num3 = sqrt((num2**2)+(num1**2))

numList=[x,y,num1, num2, round(num3.real,2)]
print(min(numList))