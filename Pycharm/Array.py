# #--------------------------------------Same Data Types In List Is Called Array------------------------------------------
# Number = [20,10,30,41,552]
# print(type(Number))
#------------------------------------------------Odd or Even------------------------------------------------------------
Number = [56,44,21,87,31,51,24,3,98,75]
oddNum = []
eveNum = []
for x in Number:
    if (x%2==0):
        eveNum.append(x)
    else:
        oddNum.append(x)
print("List of Odd Number :",oddNum)
print("List of Even Number ",eveNum)