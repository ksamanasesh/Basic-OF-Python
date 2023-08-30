# #----------------------------------------------------Hightest Value---------------------------------------------------
# value  = [0,20,45,32]
# n = 0
#
# for x in value:
#     if x>n:
#         n = x
# print(n)
#--------------------------------------------------Second Highest Value------------------------------------------------
# value = [55,37,99,98,70,42,26,19,67,1]
# num = value.sort()
#
# print("Second Highest Value : ",value[8])
# print("Third Highest Value : ",value[7])
# print("Second Lowest Value :",value[1])
# print("Third Lowest Value :",value[2])+
#
# #---------------------------------------------Second Higest value using loop--------------------------------------------
# value = [55,37,97,99,70,42,26,98,67,1]
# high  = 0
# shigh = 0
#
# for x in value:
#     if x>high:
#         shigh = high
#         high = x
#     elif x>shigh:
#         shigh = x
# print("Highest number :",high)
# print("Second highest numebr :",shigh)
#------------------------------------------------Third Highest Value-----------------------------------------------------
# value = [55,37,99,98,70,42,26,97,19,67,1]
# high = 0
# shigh = 0
# thigh = 0
# for x in value:
#     if x > high:
#         shigh = high
#         high = x
#     elif x > shigh:
#         thigh = shigh
#         shigh = x
#     elif x > thigh:
#         thigh = x
# print("Highest Value :",high)
# print("Second Highest Value :",shigh)
# print("Third Highest value :",thigh)
# # ----------------------------------------------------Lowest Value------------------------------------------------------
# value = [65,77,10,90,455,322,67,1,17]
# n = value[1]
# for x in value:
#     if x<n:
#         n = x
# print(n)
#------------------------------------------------Second & Third lowest value--------------------------------------------------
# value = [55,37,99,4,98,70,2,42,12,19,67,18]
# low = value[0]
# slow = value[0]
# tlow = value[0]
# for x in value:
#     if x<low:
#         slow = low
#         low = x
#     elif x < slow:
#         slow = x
#     elif x < tlow:
#         tlow = x
# print("Least Value :",low)
# print("Seond least value :",slow)
# print("Third least valeu :",tlow)