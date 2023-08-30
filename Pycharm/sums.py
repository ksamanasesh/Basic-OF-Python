# #----------------------------------------- Number Aren't divisible by 2 or 3------------------------------------------
# num = int(input("Enter the range :"))
# for x in range(1,num+1):
#     if (x%2!=0 and x%3!=0):
#         print(x)
# #------------------------------------------Number divisble by 7 and Muliply by 5-------------------------------------------
# value = int(input("Enter the range :"))
# for x in range(1,value+1):
#     if(x%7==0 and x%5==0):
#         print(x)
# #-------------------------------------Print All Numbers in a Range Divisible by a Given Number--------------------------
# divisible = int(input("Enter the divisible value :"))
# value = int(input("Enter the range :"))
# for x in range(1,value+1):
#     if(x%divisible==0):
#         print(x)
# #-----------------------------------------------Sum of digital number-------------------------------------------------------
# Number = int(input("Enter the Number :"))
# sum = 0
#
# while Number>0 :
#     single = Number%10
#     sum = single+sum
#     Number = Number//10
# print(sum)
# #---------------------------------------------Sum of the digit with functioin--------------------------------------------
# def Dsum(Number):
#     sum = 0
#     while Number>0:
#         Single = Number%10
#         sum = Single+sum
#         Number = Number//10
#     print("Sum of the Digit is",sum)
# Dsum(int(input("Enter the Number to sum :")))
# #--------------------------------------------------divisor of the integers---------------------------------------------
# divisor = int(input("Enter the Divisor :"))
# div = []
# smallNum = 99
# for x in range(2,divisor+1):
#     if (divisor%x==0):
#         div.append(x)
# print("Divisor of '",divisor,"' is",div)
# for x in div:
#     if x<smallNum:
#         smallNum = x
#
# print("Smallest number of the divisor is",smallNum)
# #---------------------------------------------------binary Equation------------------------------------------------------
# num = int(input("Enter the number to convert to binary :"))
# bin = num
# binary = []
# rem1 = num
# while num>0:
#     bin = num%2
#     binary.append(bin)
#     num = num//2
# binary.reverse()
# print("Binary value of",bin,"is",binary)
# #------------------------------------------------------Tables-------------------------------------------------------------
# Number = int(input("Enter the numeber for a table :"))
# for x in range(1,11):
#     print(Number,"x",x,"=",(Number*x))
# #----------------------------------------------------Amstrong Number---------------------------------------------------------
# Number = (input("Enter the Number to check it is Amstrong :"))
# intt = int(Number)
# Amstrong = 0
# power = len(Number)
# for get in Number:
#     getin = int(get)
#     amg = getin**power
#     Amstrong = Amstrong + amg
# if intt==Amstrong: print("The given number is an amstrong number",Amstrong)
# else: print("The given number is not a an amstrong number",Amstrong)
# #---------------------------------------------Counting Duplicates--------------------------------------------------------
# a = [20,40,30,20,20,30,40,10,10,50,40,30,20,30]
# nodup = 0
# for x in a :
#     for y in range(0,len(a)-1):
#         if x==a[y+1]:
#
#           print(nodup)
#----------------------------------------------------pattern--------------------------------------------------------------
# for x in range(6,0,-1):
#     for y in range(x,0,-1):
#         print("*",end=" ")
#         print("*")
# x = {"ford":"mustang","year":2020}
# x["color"]="red"
# print(x)
# a = int(5)
# print(a)
rows=int(input("Enter the Rows of the Stas :"))
for x in range(1,rows+1):
    space=" "
    star="*"
    print(space+(star*x)+space)
