# ##--------------------------------------------------No of lower case-----------------------------------------------------
# a = "Green Technology"
# lower = 0
# for x in a :
#     if x.islower():
#         lower = lower + 1
# print(f"No of LowerCase :{lower}")
# #---------------------------------------------------No of Upper Case--------------------------------------------------------
# b = "I Am IronMan"
# upper = 0
# for y in b :
#     if y.isupper():
#         upper = upper + 1
# print(f"No of UpperCase :{upper}")
# # ------------------------------------------------------------------------------------------------------------------------
c = input("Enter the sentence :")
list = c.split()

for x in list:
    print(x)
