while 1:  #파일의 끝을 만나면 EOF 에러 -> TRY-CATCHE 사용해서 예외처리
    try:
        a,b=map(int,input().split())
        print(a+b)
    except EOFError:
        break
