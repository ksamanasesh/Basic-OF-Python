print("Hello World")

a = "Hello"
print(a)

b = "World"
print(b)

print(a+b)
print(type(a+b))

#---------------------------------------------------Slicing------------------------------------------------------

c = "Green Technology Porur"
d = "Student name is Butler"

print(c[0:6])
print(c[-22:-17])
print(c[0:-17])
print(c[-22:5])

print(c[6:16])
print(c[-16:-6])
print(c[6:-6])
print(c[-16:16])

print(c[17:23])
print(c[-5:-1]+c[-1])
print(c[17:-1]+c[-1])
print(c[-5:23])

print(d[0:7]+d[16:19])

# #----------------------------------------------String Manipulation---------------------------------------------------

a = "       Manasesh"
print (a.lstrip())
b = "Manasesh          "
print (b.rstrip())
c = "K S A Manasesh"
print (c.removeprefix("K S A "))
print (c.removesuffix("sesh"))

a = "Butler scored 75 runs in 35 balls against India"
print(a)
#
print (a.count("scored"))
print (a.index("75"))
print (a.upper())
print (a.lower())
print (a.capitalize())
print (a.title())
print (a.isupper())
print (a.islower())
print (a.istitle())
ab = (a.replace("Butler","Dhoni"))
print(ab)
#----------------------------------------------List Slicing & Manipulation--------------------------------------------
b = a.split()
print (b)

print ((b[7])[0:5])
print ((b[7])[-7:-2])
print ((b[7])[0:-2])
print ((b[7])[-7:5])

print ((b[8])[0:3])
print ((b[8])[-5:-2])
print ((b[8])[0:-2])
print ((b[8])[-5:3])

b=["India","won","the","world","cup","in"]

print (b.count("won"))
b.append("2011")
print (b)
b.insert(3,"T20")
print (b)
b.pop(3)
print(b)
b.reverse()
print(b)
b.sort()
print(b)
b.clear()
print(b)

#-----------------------------------------------------Dictionary-----------------------------------------------------

a = {"Red":"IronMan","Blue":"Captain America","Green":"Hulk","Black":"Black Widow"}

print (a)

print (a.keys())
print (a.values())
print ("Value of Red",a["Red"].count("n"))
print ("Index Of",a["Blue"].index("t"))
print (a["Green"].istitle())
print (a["Black"].lower())
print (a)
print (a["Red"].upper())


b = {"CSK":["Dhoni","Raina","Jadeja"],"RCB":["Virat","Faf","Maxwell"],"MI":["Rohit","Ishan","Pollard"]}
print (b)
print (b.values())
print (b.keys())
print (b["CSK"].pop(1))
print (b["RCB"].count("Faf"))
b["MI"].append("Acher")
print (b)
b["CSK"].insert(2,"Conway")
print (b)
b["RCB"].reverse()
print (b)
b["MI"].sort()
print (b)
b["CSK"].clear()
print (b)
#----------------------------------------------------Tuple------------------------------------------------------------
a = ("IronMan","Captain America","SpiderMan","Hulk","Thor")
print (a)
print(a.count("Hulk"))
print (a.index("SpiderMan"))
print (a[4].upper())
print (a[1][8::])
#------------------------------------------------------Set------------------------------------------------------------
a = {"SuperMan","BatMan","Flash","WonderWomen","DeadPool","SpiderMan"}
b = {"IronMan","Captain America","Thor","AntMan","Strange","SpiderMan"}
print (a)
print (b)
a.add("Thanos")
print (a)
print (a.difference(b))
print (a.union(b))
print ((a.intersection(b)))
#-----------------------------------------------------Implicit--------------------------------------------------------
a = 25
print (a)
print(type(a))
b = 22.5
print (b)
print(type(b))
print (a+b)
print (type(a+b))
#-----------------------------------------------------Expltict--------------------------------------------------------
a = ["IronMan","Captian Amerrica","Hulk","Captain Marvel"]
print((a))
print(type(a))
b = set(a)
print (b)
print (type(b))
a=10

c=str(a)
print (c)
print (type(c))

#--------------------------------------------------Escape Sequence-----------------------------------------------------
print ("Manasesh\nS Smith")              #To Print in Next Line
print ("\"Manasesh\"")
print ("K\tS\tA\tManasesh")
print ("\\Manasesh\\")
#-----------------------------------------------------Summa--------------------------------------------------------------
a=20
a+=a
print(a)
a="Banana"
b="Apple"
print(a+b)
p = "Manasesh"
b=p.__contains__("a")
print(b)
a = 123
b = str(a)
print(b)
c = list(b)
print(c)
for x in range(5,11):
    print(x)
a = [1,2,3,4]
a.reverse()
# print(a)
a = "Priya"
print(f'{a}heloo')