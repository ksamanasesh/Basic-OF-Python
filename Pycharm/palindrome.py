a = int(input("Enter the panlidrome number"))
b=a
num = 0
while a>0:
    rem = a%10
    num = num*10+rem
    a = a//10
print(num)

if num==b:
    print("The number is Palindrome")
else:
    print(("The number is not Palindrome"))