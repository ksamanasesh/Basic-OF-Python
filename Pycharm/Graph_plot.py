import matplotlib.pyplot as cg
import numpy as np
import pandas as pa
#-----------------------------------------------------Line Graph--------------------------------------------------------
# x = [8,9,8.5,8.5,9,8]
# y = [5,5,5,6,6,6]
# x = [2,2.5,3]
# y = [5,6,5]
# x1 = [4,4,5,4]
# y1 = [5,6,5.5,5]
# x2 = [6,6,6,7,7,7]
# y2 = [5,6,5.5,5.5,5,6]
# x3 = [8,9,8.5,8.5,9,8]
# y3 = [5,5,5,6,6,6]
# cg.plot(x,y)
# cg.plot(x1,y1)
# cg.plot(x2,y2)
# cg.plot(x3,y3)
# cg.xlim(1,10)
# cg.ylim(1,10)
# cg.xlabel("X-Axis")
# cg.ylabel("Y-Axis")
# cg.title("First graph")
# cg.show()
#---------------------------------------------------Bar Graph-----------------------------------------------------------
# overs = [5,10,15,20]
# runs = [48,97,146,202]
#
# cg.bar(overs,runs)                                        # Bar Graph
# cg.xlabel("Overs")
# cg.ylabel("Runs")
# cg.title("Score")
# cg.legend("Overs","Runs")
# cg.show()
#--------------------------------------------------HistGram---------------------------------------------------------------
# age = [12,10,23,21,22,23,22,23,21,23,19,18,19,17,18,18,17,18,16,19,17,18,21]         # Histrogram
# range = (0,50)
# bins = 5
# cg.hist(age,bins,range,color="green",histtype="bar",rwidth=0.5)
# cg.xlabel("Ages")
# cg.ylabel("Gamers")
# cg.title("Gamers Age")
# cg.show()
#----------------------------------------------------Pie Chat------------------------------------------------------------
# timing = ["Sleep","Gaming","Coding","Music","Movies & Series","Others"]               # Pie Chat
# Tsize = [8,4,3,2,2,5]
# colors = ["green","yellow","red","blue","purple","gray"]
# cg.pie(Tsize,labels=timing,colors=colors,startangle=90,radius=1)
# cg.legend()
# cg.show()
# #----------------------------------------------------Frequency----------------------------------------------------------
# freq = np.arange(0,2*(np.pi),.1)
# levl = np.sin(freq)
# cg.plot(freq,levl)
# cg.show()
# #------------------------------------------------------------------------------------------------------------------------
# v1 = [2,2.5,3]
# v2 = [6,5,6]
# e1 = [5,4,4,5,4,4,5]
# e2 = [5,5,6,6,6,5.5,5.5]
# n1 = [6,6,7,7]
# n2 = [5,6,5,6]
# k1 = [8,8,8.5,8,8.5,8,8]
# k2 = [5,5.5,6,5.5,5,5.5,6]
# a1 = [9.5,10,10.5]
# a2 = [5,6,5]
# n21 = [11.5,11.5,12.5,12.5]
# n22 = [5,6,5,6]
# t1 = [13,14,13.5,13.5]
# t2 = [6,6,6,5]
#
# j1 = [4,4,4.5,4.5,5,4]
# j2 = [9.5,9,9,10,10,10]
# a21 = [5.5,6,6.5]
# a22 = [9,10,9]
# y1 = [7,7.5,7.5,7.5,8]
# y2 = [10,9.5,9,9.5,10]
# a31 = [8.5,9,9.5]
# a32 = [9,10,9]
#
# cg.xlim(1,15)
# cg.ylim(1,15)
# cg.plot(v1,v2)
# cg.plot(e1,e2)
# cg.plot(n1,n2)
# cg.plot(k1,k2)
# cg.plot(a1,a2)
# cg.plot(n21,n22)
# cg.plot(t1,t2)
# cg.plot(j1,j2)
# cg.plot(a21,a22)
# cg.plot(y1,y2)
# cg.plot(a31,a32)
# cg.show()
# # #--------------------------------------------------Data Frame--------------------------------------------------------
# trop = {
#     "t1":["CSK","KKR","RR","SRH","GT","MI"],
#     "champ":[5,2,1,1,1,5]
# }
# champ = pa.DataFrame(trop)
# champ.plot("t1","champ",kind="scatter",color="red",marker="o",s=25)
# cg.xlabel("Team")
# cg.ylabel("Champion Trophy")
# cg.title("IPL Champions")
# cg.show()
# d1 = {
#     "x":[5,6,4,8,6],
#     "y":[9,4,6,1,3],
#     "x1":[1,2,3,4,5],
#     "y1":[6,4,7,1,3]
# }
#
# data = pa.DataFrame(d1)
# data.plot(x="x",y="y",kind="scatter")
#
# cg.xlabel("X Axis")
# cg.ylabel("Y Axis")
# cg.show()
# #----------------------------------------------------Excel Sheet---------------------------------------------------------
score = pa.read_excel("D:\Python\Files Analysing\IPl score.xlsx")
score.plot("name","sco",kind="line",color="y",marker="o",)
cg.xlabel("Player")
cg.ylabel("Highest Score")
cg.title("IPl Highest Score")
cg.show()

