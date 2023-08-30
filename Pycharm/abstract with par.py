from abc import ABC,abstractmethod

class school(ABC):
    @abstractmethod
    def details(self,name,mail,father,phone,add):
        pass
    @abstractmethod
    def mark(self,m1,m2,m3,m4,m5):
        pass
class student1(school):
    def details(self,name,mail,father,phone,add):
        print("\nStudent 1 Details :")
        print("\nName :",name,"\ne-Mail :",mail,"\nPhone Number :",phone,"\nFather Name :",father,"\nAddress :",add)
    def mark(self,m1,m2,m3,m4,m5):
        print("\nStudent1 Mark List :")
        print("\nTamil :", m1, "\nEnglish :", m2, "\nMaths :", m3, "\nScience :", m4, "\nSocial :", m5)
class student2(school):
    def details(self,name,mail,father,phone,add):
        print("\nStudent 2 Details :")
        print("\nName :",name,"\ne-Mail :",mail,"\nPhone Number :",phone,"\nFather Name :",father,"\nAddress :",add)
    def mark(self,m1,m2,m3,m4,m5):
        print("\nStudent 2 Makr List :")
        print("\nTamil :", m1, "\nEnglish :", m2, "\nMaths :", m3, "\nScience :", m4, "\nSocial :", m5)
s = student1()
ss = student2()

s.details("Rahul","rahul@gmail.com","James","78984561","Chennai")
s.mark(98,97,100,66,78)

ss.details("Rock","rock@gmail.com","star","32154678","Delhi")
ss.mark(77,55,47,35,98)
