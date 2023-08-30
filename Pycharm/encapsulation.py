class school:
    def __init__(self):
        self.__name=""
        # self.__pass=""
    def setusername(self):
        self.__name = "Rahul"
    def getusername(self):
        return self.__name
class student(school):
    def login(self):
        print("login by Student :",self.getusername())

ss=student()
ss.setusername()
ss.getusername()
ss.login()
