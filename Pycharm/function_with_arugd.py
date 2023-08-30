# #-----------------------------------------------Using For Loop----------------------------------------------------------
# a = ("IronMan","Captain America","Hulk","SpiderMan","Strange")
#
# def mcu(b):
#     for i,x in enumerate(b):
#         print("Avenger ",i+1," :",x)
# mcu(a)
# #--------------------------------------------------Tuple----------------------------------------------------------------
#
# a = ("IronMan","Captain America","Hulk","SpiderMan","Thor")
#
# def mv(*b):
#     print("Avenger 1 :",a[1])
#     print("Avenger 2 :",a[0])
#     print("Avenger 3 :",a[4])
#     print("Avenger 4 :",a[3])
#     print("Avenger 5 :",a[2])
# mv(a)
# #--------------------------------------------------Dictionary-----------------------------------------------------------
#
# a={"Team 1":"Dhoni","Team 2":"Rohit","Team 3":"Hardik","Team 4":"Virat","Team 5":"Warner"}
# def ipl(**b):
#     print("CSK Captain :",b["Team 1"])
#     print("Mi Captain :",b["Team 2"])
#     print("Gt Captain :",b["Team 3"])
#     print("Rcb Captain :",b["Team 4"])
#     print("Dc Captain :",b["Team 5"])
# ipl(**a)