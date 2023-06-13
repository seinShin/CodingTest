import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

flag=False
while len(s) <= len(t):
    if s == t:
        flag= True

    # 끝 문자열
    x = t[-1]    
    t = t[:-1]

    if x == 'A':
        continue
    elif x == 'B':
        t = t[::-1]
        
#검사
if flag:
    print(1)
else:
    print(0)