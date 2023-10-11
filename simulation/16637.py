# 16637 괄호 추가하기
n = int(input())
s = input()
rst = -1*(2**31)


def oper(num1, oper, num2):
    if oper == '+':
        return num1+num2
    elif oper == '-':
        return num1-num2
    elif oper == '*':
        return num1*num2

def dfs(idx, val):
    global rst
    if idx == n-1:
        rst = max(rst, val)
        return 
    
    if idx+2 < n:
        dfs(int(idx+2), oper(val, s[idx+1], int(s[idx+2])))
        
    if idx+4 < n:
        dfs(int(idx+4), oper(val, s[idx+1], oper(int(s[idx+2]), s[idx+3], int(s[idx+4]))))
        
    
dfs(0, int(s[0]))
print(rst)