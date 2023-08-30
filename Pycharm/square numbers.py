# #-------------------------------------------------square numeber---------------------------------------------------
# Numbers = []
# def Square(snum):
#     for x in range(1,snum+1):
#         yield x
#
# SquareNum = Square(int(input("Enter the Number :")))
#
# for z in SquareNum:
#     Numbers.append(z**2)
# print(Numbers)
#-------------------------------------------------Cube Numeber----------------------------------------------------
CubeNumbers = []
def Cube(cnum):
    for x in range(1,cnum+1):
        yield x
Number = Cube(int(input("Enter the number :")))

for z in Number:
    CubeNumbers.append(z**3)
print(CubeNumbers)
