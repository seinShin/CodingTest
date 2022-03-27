''' def priTest(n):
    i=1
    rst=0
    while i*i<n:
        if n%i ==0:
            rst +=2
        i+=1
    if i*i == n:
        rst +=1
    return rst
 '''
 
import math
import sys
input = sys.stdin.readline
 
def isPrime(n):
    if n == 1 : return False
     
    sq = int(math.sqrt(n))
     
    for i in range(2,sq+1):
        if n % i == 0 : return False
    return True


m, n = map(int, input().split())
for i in range(m, n+1):
    if(isPrime(i)):
        print(i)
  