n1=int(input("enter num 1: "))
op=input("enter or operator +,-,*,/  :")
n2=int(input("enter a n2 : "))
if op== "+":
    print("result :",n1+n2)
elif op=="-":
    print("result :",n1-n2)
elif op=="/" :
    if n2==0:
        print("enter a valid number")
    print("result :",n1/n2)
elif op=="*":   
    print("result :",n1*n2)
else:
    print("enter a valid operator")