class code1 :
    def code(self):
        password = input("Enter the password :")
        if len(password) > 25 :
            print("Your password can contains maximum 25 characters")
        elif len(password) < 10 :
            print("Your password must contain atleast 10 character")
        else:
            print(password)
class code2(code1.code()) :
    def alpha(self):
        num = "1234567890"
        for x in num:
            if x not in code1:
                print()


