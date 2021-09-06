A, B = map(int,input().split()) # split으로 공백 입력 그냥 input 사용하면 문자열 형식, 따라서 map사용
 

if(A>B):
    print(">")
elif (A<B):
    print("<")
else:
    print("==")
    
