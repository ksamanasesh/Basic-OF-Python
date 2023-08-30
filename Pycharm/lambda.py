# #---------------------------------------------------lambda------------------------------------------------------------
# add = lambda a,b:a+b
# print(add(10,20))
# #-------------------------------------------------Odd or Even---------------------------------------------------------
# number = lambda a: "Even Number" if (a%2==0) else "Odd Number"
# print(number(int(input("Enter the number :"))))
#---------------------------------------------------lambda Task---------------------------------------------------------
Number = [56,44,21,87,31,51,24,3,98,75]
OddNum = []
EvenNum = []
for x in Number:
    check = lambda x:EvenNum.append(x) if (x%2==0) else OddNum.append(x)
    check(x)
print("Odd Number of the list",OddNum)
print("Even Number of the list",EvenNum)
