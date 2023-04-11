import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def cantore(lst, start, length):
    temp = length // 3
    
    if temp == 0:
        return
    
    for i in range(start+temp, start+temp*2):
        lst[i] = ' '
    
    cantore(lst, start, temp)
    cantore(lst, start+temp*2, temp)
    

while True:
    try:
        n = int(input())
        
        if n == '':
            break
        else:
            lst = ['-' for i in range(3**n)]
            cantore(lst, 0, 3**n)
            ans=''
            for i in lst:
                ans+=i
            print(ans)
                
    except EOFError:
        break
