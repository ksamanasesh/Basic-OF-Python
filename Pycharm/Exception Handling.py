# #---------------------------------------------Zero Division Error---------------------------------------------------------
# print(1)
# print(2)
# print(3)
# try :
#     print(4/0)
# except ZeroDivisionError:
#     print("Can't Divide by 0")
# else :
#     print("No error case")
# finally:
#     print("End of Execption")
# print(5)
# print(6)
#-------------------------------------------------Value error--------------------------------------------------------------
try:
    num = int(input("Enter your Number :"))
    print(num)
except ValueError:
    print("Invalid Input")
else:
    print("Verified")
finally:
    print("End Of Exception")