#-------------------------------------------------Single Inheritance----------------------------------------------------
# class student :
#     def name(self,reg,ph):
#         print("Register number :",reg)
#         print("Phone Number ",ph)
# class detail (student):
#     def father(self,name):
#         print("Father's Name :",name)
#     def mother(self,mname):
#         print("Mother's name :",mname)
# info = detail()
# info.name((int(input("Enter the register number :"))),(int(input("Enter the Phone Number :"))))
# info.father(input("Enter the father's name :"))
# info.mother(input("Enter the mother's name :"))
# #--------------------------------------------------Multiple Inheritance---------------------------------------------------
# class student :
#     def name(self,sname):
#         print("Student Name :",sname)
# class teacher :
#     def teach(self,tname):
#         print("Teacher Name :",tname)
# class principal(student,teacher):
#     def pricn(self,pname):
#         print("Principal Name :",pname)
#
# info = principal()
# info.pricn("Robert")
# info.teach("Maths Teacher")
# info.name("Rahul")
# #-----------------------------------------------MultiLevel Inheritance--------------------------------------------------
class Gfather:
    def grandfather(self,gname):
        print("Grand Father's Name :",gname)
class father(Gfather):
    def ffather(self,fname):
        print("Father's Name :",fname)
class son(father):
    def sson(self,sname):
        print("Son's Name :",sname)
fam = son()
fam.grandfather("Ramesh")
fam.ffather("Suresh")
fam.sson("Rahul")
# #----------------------------------------------Hirarchical Inheritance------------------------------------------------
# class student :
#     def name(self,sname):
#         print("Student Name :",sname)
# class teacher(student):
#     def tname(self):
#         print("Accesed with Teacher Class :")
# class principal(student):
#     def pname(self):
#         print("Accesed with Principle Class")
#
# pri = principal()
# pri.pname()
# pri.name("Rahul")
#
# tea = teacher()
# tea.tname()
# tea.name("Rahul")
#--------------------------------------------------Hybird Inheritance--------------------------------------------------
# class student:
#     def stu(self,sname):
#         print("Student Name :",sname)
# class teacher(student):
#     def teach(self):
#         print("Accessed with teacher class :")
#     def tname(self,name):
#         print("Teacher Name :",name)
# class VicePrincipal(student):
#     def vp(self):
#         print("Accessed with Vice Principle Class :")
#     def vpname(self,vname):
#         print("Vice Pricipal Name :",vname)
# class principle(teacher,VicePrincipal):
#     def hm(self):
#         print("Accessed with Pricipal Class :")
#
# tea = teacher()
# tea.teach()
# tea.stu("Rahul")
#
# vpp = VicePrincipal()
# vpp.vp()
# vpp.stu("Rahul")
#
# pri = principle()
# pri.hm()
# pri.vpname("Sathiya")
# pri.tname("Bhavani")
# pri.stu("Rahul")
