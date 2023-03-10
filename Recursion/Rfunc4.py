def isPalindrome(cnt, str):
    if len(str) <=1:
        print(1, cnt)
    else:
        if str[0:] == str[:-1]:
            cnt+=1
            return isPalindrome(cnt, str[1:-2])
        else:
            print(0, cnt) 
    
    
n = int(input())
for _ in range(n):
    n = input()
    isPalindrome(1, n)