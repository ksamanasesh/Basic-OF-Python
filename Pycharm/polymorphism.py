#----------------------------------------------Overriding--------------------------------------------------------------
# class csk:
#     def captain(self,name):
#         print("Csk Captain :",name)
# class mi:
#     def captain(self,name):
#         print("Mi Captain :",name)
#
# c = csk()
# m = mi()
#
# for x in (c.captain("Dhoni"),m.captain("Rohit")):
#     print(x)
# #----------------------------------------------overring with construtor---------------------------------------------
class csk:
    def __init__(self,name):
        self.name = name
    def captain(self):
        print("Csk Captain :",self.name)
class mi:
    def __init__(self,name):
        self.name=name
    def captain(self):
        print("Mi Captain :",self.name)

# c = csk("Dhoni")
# m = mi("Rohit")
#
# for x in (c.captain(),m.captain()):
#     print(x)

# c.captain()
# m.captain()

