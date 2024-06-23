from sys import stdin
import math

t = int(stdin.readline())

def isPrime(n):
    if n == 1 : return False
     
    sq = int(math.sqrt(n))
     
    for i in range(2,sq+1):
        if n % i == 0 : 
            return False
    return True

for i in range(t):
    n = int(stdin.readline())
    
    a = int(n/2)
    b = int(n/2)

    for j in range(int(n/2)):
        if(isPrime(a) == True and isPrime(b) == True):
            print(a,b)
            break
        else:
            a -= 1
            b += 1  
            


