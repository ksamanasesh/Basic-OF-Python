from abc import ABC,abstractmethod
class school(ABC):

    @abstractmethod
    def details(self):
        pass
    @abstractmethod
    def marks(self):
        pass
class student1(school):
    def details(self,name,mail,phone,father,address):
        print("\nStudent 1 Details :")
        print("\nName :",name,"\ne-Mail :",mail,"\nPhone Number :",phone,"\nFather Name :",father,"\nAddress :",address)
    def marks(self,m1,m2,m3,m4,m5):
        print("\nStudent 1 Mark List :")
        print("\nTamil :",m1,"\nEnglish :",m2,"\nMaths :",m3,"\nScience :",m4,"\nSocial :",m5)
class student2(school):
    def details(self,name,mail,father,phone,address):
        print("\nStudent 2 Details :")
        print("\nName :",name,"\ne-Mail :",mail,"\nPhone Numeber :",phone,"\nFather Name :",father,"\nAddress :",address)
    def marks(self,m1,m2,m3,m4,m5):
        print("\nStudent 2 Mark List :")
        print("\nTamil :",m1,"\nEnglish",m2,"\nMaths :",m3,"\nScience :",m4,"\nSocial :",m5)

s = student1()
ss = student2()

s.details("Rahul","rahul@gmail.com",789456132,"Guru","Chennai")
s.marks(95,90,100,56,35)

ss.details("James","james@gmail.com",456123798,"Arul","Vellore")
ss.marks(78,89,54,66,91)

