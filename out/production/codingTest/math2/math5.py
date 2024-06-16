import math
import sys
    

def isPrime(n):
    if n == 1 : return False
     
    sq = int(math.sqrt(n))
     
    for i in range(2,sq+1):
        if n % i == 0 : 
            return False
    return True

alist = list(range(2,246912))  #범위
slist = []
for i in alist :
    if isPrime(i):
        slist.append(i)

while True:
    n = int(sys.stdin.readline())       
    count =0
    if n == 0:
        break
    
    for i in slist:
        if n < i <= n*2:
            count +=1
    print(count)
            
        