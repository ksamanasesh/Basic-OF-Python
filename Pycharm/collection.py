from collections import Counter
# #-----------------------------------------------------Counter-------------------------------------------------------------
# # To the count the elements
# list = [1,2,1,2,2,3,1,1,1,4]
# cont = Counter(list)
# print(cont)
#
# name = "Priya"
# con = Counter(name)
# print(con)
#---------------------------------------------------OderedDict--------------------------------------------------------------
from collections import OrderedDict
order = OrderedDict()
order["CSK"]=3
order["Mi"]=4
order["RCB"]=0
for ipl,win in order.items():
    print(ipl,win)
order["KKR"]=2
order["CSK"]=4
print("***********After Update************")
for ipl,win in order.items():
    print(ipl,win)
# #------------------------------------------------------Chain Map----------------------------------------------------------
# from collections import ChainMap
#
# group1 = {"Csk":3,"Mi":4,"Rcb":0}
# group2 = {"Kkr":2,"Rr":1,"Srh":1}
#
# link = ChainMap(group1,group2)
# print(link)
#
# for x,y in link.items():
#     print(x,y)
# # ----------------------------------------------------namedtuple----------------------------------------------------------
# from collections import namedtuple
#
# Team = namedtuple("Team",["CSK","RCB","MI","KKR","RR"])
#
# ipl = Team("Captain",'Dhoni','Virat','Rohit','Rana','Samson')
# print(Team._make(ipl))
# #------------------------------------------------------deque--------------------------------------------------------------
# from collections import deque
# Teams = deque(["CSK","MI","RCB","GL"])
# print("Standar",Teams)
# Teams.append("KKR")
# print("Added",Teams)
# Teams.appendleft("RR")
# print("Added Left",Teams)
# Teams.pop()
# print("POP",Teams)
# Teams.popleft()
# print("Pop left",Teams)
# #------------------------------------------------------User list-----------------------------------------------------------
# from collections import UserList
#
# class Marvel(UserList):
#     def append(self,m = None):
#         raise RuntimeError("Can't append in Marvel")
#     def pop(self,n = None):
#         raise RuntimeError("Can't Pop in Marvel")
# list = Marvel(["IronMan","Captain America","Thor","SpiderMan"])
# print("Marvel list :",list)
# list.append("SuperMan")
# print(list)
# list.pop()
# print(list)
#--------------------------------------------------------User String---------------------------------------------------
# from collections import UserString
#
# class Marvel(UserString):
#     def upper(self,m =None):
#         raise RuntimeError("Can't Use Upper in Marvel")
#     def replace(self,m = None):
#         raise RuntimeError("Can't replace in Marvel")
#
# team = Marvel("IronMan")
# print(team)
# # team.upper()
# # print(team)
# team.replace()
# print(team)
#-----------------------------------------------------User Dict---------------------------------------------------------
# from collections import UserDict
#
# class Marvel(UserDict):
#     def values(self, m = None):
#         raise RuntimeError("Can't get the values")
#     def keys(self, m =None):
#         raise RuntimeError("can't get the Keys")
# team = Marvel({"IronMan":"SpiderMan","Captain America":"Black Widow","Thor":"Hulk"})
# print(team)
# team.values()
# print(team)