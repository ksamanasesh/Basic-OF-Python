name = input("Enter Your name")
reg = (input("Enter your Register number"))
m1 = int(input("Enter your mark 1 :"))
m2 = int(input("Enter your mark 2 :"))
m3 = int(input("Enter Your mark 3:"))
m4 = int(input("Enter your mark 4 :"))
m5 = int(input("Enter your mark 5 :"))
mark =[m1,m2,m3,m4,m5]

for i,m in enumerate(mark):
    if m>=90:
        print("mark",i+1,": A+")
    if m>=80 and m<90:
        print("mark",i+1,": A")
    if m>=70 and m<80:
        print("mark",i+1,": B")
    if m>=60 and m<70:
        print("mark",i+1,": C")
    if m>=50 and m<60:
        print("mark",i+1,": D")
    if m>=40 and m<50:
        print("mark",i+1,": E")
    if m<40:
        print("mark",i+1,": F")
