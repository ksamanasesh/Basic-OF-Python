class write:
    def student(self):
        file = open("D:\Python\students.txt","w")
        file.write("\nName : Guido\nRegister No : 789456\ne-Mail : james@gamil.com\nPhone Numeber : 6541239870\nFather Name : James\nPlace : Chennai")
class read:
    def details(self):
        file = open("D:\Python\students.txt","r")
        print(file.read())
w = write()
r = read()
w.student()
r.details()