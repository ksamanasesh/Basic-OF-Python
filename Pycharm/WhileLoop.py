a = int(input("Enter the number :"))
ob=0
while a>0:
    rem = a%10
    ob = ob*10+rem
    a   = a//10
    print (ob)

