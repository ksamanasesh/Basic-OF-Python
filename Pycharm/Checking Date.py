#----------------------------------------------Checking valid date--------------------------------------------------------
date = int(input("Enter the date :"))
mon = int(input("Enter the Month :"))
year = int(input("Enter the Year :"))

DD = print("You Entered Date :",date,"/",mon,"/",year)

if (mon==1 and mon==3 and mon==5 and mon==7 and mon==8 and mon==10 and mon==12):
    md = 31
elif (mon==4 or mon==6 or mon==9 or mon==11):
    md = 30
else:
    if (year%4==0):
        md = 29
    else:
        md = 28
if (mon<1 or mon>12):
    print("Invali Date")
elif (date<1 or date>md):
    print("Invalid Date")
else:
    print("Date Verified Succesfully",date,"/",mon,"/",year)

