cal = int(input())

if((cal%4==0) & (cal%100!=0)):
    print("1")
elif(cal%400==0):
    print("1")
else:
    print("0")