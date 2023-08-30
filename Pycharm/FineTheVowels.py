word = "Green Technology"

for x in (word):

    if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):

        without = word.replace(x,"")
        out = without
        print(out)

